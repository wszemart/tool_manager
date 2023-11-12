import logging
import os
from tempfile import NamedTemporaryFile
from typing import Dict, List, Union

import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from weasyprint import HTML

from .forms import MachineForm
from .models import Machine

logger = logging.getLogger(__name__)
Breadcrumb = Dict[str, Union[str, str]]


class BreadcrumbMixin:
    def get_context_data(self, **kwargs) -> Dict[str, Union[str, List[Breadcrumb]]]:
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = self.get_breadcrumbs()
        return context

    def get_breadcrumbs(self) -> List[Breadcrumb]:
        breadcrumbs = [{"title": "Strona główna", "url": reverse("app-home")}]

        if isinstance(self, MachineDetailView):
            machine = self.get_object()
            breadcrumbs.append(
                {
                    "title": machine.name,
                    "url": reverse("machine-detail", kwargs={"pk": machine.pk}),
                }
            )
        elif isinstance(self, MachineCreateView):
            breadcrumbs.append({"title": "Utwórz nową maszynę", "url": reverse("machine-create")})
        elif isinstance(self, MachineUpdateView):
            machine = self.get_object()
            breadcrumbs.append(
                {
                    "title": machine.name,
                    "url": reverse("machine-detail", kwargs={"pk": machine.pk}),
                }
            )
            breadcrumbs.append(
                {
                    "title": "Aktualizuj",
                    "url": reverse("machine-update", kwargs={"pk": machine.pk}),
                }
            )

        return breadcrumbs


@login_required
def home(request: HttpRequest) -> HttpResponse:
    user = request.user
    logger.info(f"User {user} home view accessed.")
    return render(request, "machines/machine.html", {"title": "Home"})


class MachineListView(BreadcrumbMixin, ListView):
    model = Machine
    template_name = "machines/machines_list.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        user = request.user
        logger.info(f"Machine List View accessed by user {user}")
        return super().get(request, *args, **kwargs)


class MachineDetailView(BreadcrumbMixin, DetailView):
    model = Machine
    template_name = "machines/machine_detail.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        user = request.user
        logger.info(f"Machine Detail View accessed by user {user}")
        return super().get(request, *args, **kwargs)


class MachineCreateView(LoginRequiredMixin, BreadcrumbMixin, PermissionRequiredMixin, CreateView):
    permission_required = "machines.add_machine"
    model = Machine
    template_name = "machines/machine_form.html"
    form_class = MachineForm

    def form_valid(self, form: MachineForm) -> HttpResponse:
        form.instance.author = self.request.user
        logger.info(f"Machine {form.instance.name} created by {form.instance.author}.")
        return super().form_valid(form)


class MachineUpdateView(BreadcrumbMixin, LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "machines.change_machine"
    model = Machine
    template_name = "machines/machine_form.html"
    fields = ["name", "description"]

    def form_valid(self, form: MachineForm) -> HttpResponse:
        form.instance.author = self.request.user
        logger.info(f"Machine {form.instance.name} updated by {form.instance.author}.")
        return super().form_valid(form)


class MachineDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "machines.delete_machine"
    model = Machine
    template_name = "machines/delete_confirm.html"
    success_url = "/"

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        machine = self.get_object()
        user = request.user
        logger.info(f"Machine {machine.name} deleted by user {user}")
        return super().post(request, *args, **kwargs)


def generate_csv(request: HttpRequest) -> HttpResponse:
    machines = Machine.objects.all()
    data = []

    for machine in machines:
        tools = machine.tools.all()
        for tool in tools:
            data.append(
                {
                    "Nr narzędzia": tool.tool_nr,
                    "Promień": tool.radius,
                    "Długość całkowita": tool.total_length,
                    "Długość poza oprawką": tool.outside_holder,
                    "Maszyna": machine.name,
                    "Typ oprawki": tool.holder.get_holder_type_display(),
                    "Typ freza": tool.tool.get_tool_type_display(),
                }
            )

    df = pd.DataFrame(data)
    response = HttpResponse(content_type="text/csv; charset=utf-8")
    response["Content-Disposition"] = 'attachment; filename="data-csv.csv"'
    csv_to_data = df.to_csv(None, index=False, encoding="utf-8")

    response.write(csv_to_data)

    logger.info(f"CSV generation completed by user: {request.user}")

    return response


def generic_pdf(request: HttpRequest) -> HttpResponse:
    os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")

    machines = Machine.objects.all()
    data = []

    for machine in machines:
        tools = machine.tools.all()
        for tool in tools:
            data.append(
                {
                    "tool_number": tool.tool_nr,
                    "radius": tool.radius,
                    "total_length": tool.total_length,
                    "outside_holder": tool.outside_holder,
                    "machine": machine.name,
                    "holder_type_display": tool.holder.get_holder_type_display(),
                    "tool_type_display": tool.tool.get_tool_type_display(),
                }
            )

    content = render_to_string("machines/root.html", {"machines": data})

    with NamedTemporaryFile(delete=False, suffix=".pdf") as file:
        HTML(string=content).write_pdf(file.name)

        file.seek(0)
        pdf_content = file.read()

    response = HttpResponse(pdf_content, content_type="application/pdf")
    response["Content-Disposition"] = 'inline; filename="generated.pdf"'

    os.remove(file.name)

    logger.info(f"PDF generation completed by user: {request.user}")

    return response
