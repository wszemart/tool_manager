import logging
from typing import Dict, List, Union

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .forms import HolderForm
from .models import Holder

logger = logging.getLogger(__name__)
Breadcrumb = Dict[str, Union[str, str]]


class BreadcrumbMixin:
    def get_context_data(self, **kwargs) -> Dict[str, Union[str, List[Breadcrumb]]]:
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = self.get_breadcrumbs()
        return context

    def get_breadcrumbs(self) -> List[Breadcrumb]:
        breadcrumbs = [{"title": "Strona główna", "url": reverse("app-home")}]

        if isinstance(self, HolderListView):
            breadcrumbs.append({"title": "Tabela oprawek", "url": reverse("holder")})
        elif isinstance(self, HolderDetailView):
            holder = self.get_object()
            breadcrumbs.append({"title": "Tabela oprawek", "url": reverse("holder")})
            breadcrumbs.append(
                {
                    "title": f"Oprawka: {holder.get_holder_type_display()}",
                    "url": reverse("holder-detail", kwargs={"pk": holder.pk}),
                }
            )
        elif isinstance(self, HolderCreateView):
            breadcrumbs.append({"title": "Tabela oprawek", "url": reverse("holder")})
            breadcrumbs.append({"title": "Utwórz nową oprawkę", "url": reverse("holder-create")})
        elif isinstance(self, HolderUpdateView):
            holder = self.get_object()
            breadcrumbs.append({"title": "Tabela oprawek", "url": reverse("holder")})
            breadcrumbs.append(
                {
                    "title": "Aktualizuj oprawkę",
                    "url": reverse("holder-update", kwargs={"pk": holder.pk}),
                }
            )

        return breadcrumbs


class HolderListView(BreadcrumbMixin, ListView):
    model = Holder
    template_name = "holders/holder.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        user = request.user
        logger.info(f"Holder List View accessed by user {user}")
        return super().get(request, *args, **kwargs)


class HolderDetailView(BreadcrumbMixin, DetailView):
    model = Holder
    template_name = "holders/holder_detail.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        user = request.user
        logger.info(f"Holder Detail View accessed by user {user}")
        return super().get(request, *args, **kwargs)


class HolderCreateView(BreadcrumbMixin, LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "holders.add_holder"
    model = Holder
    template_name = "holders/holder_form.html"
    form_class = HolderForm
    success_url = reverse_lazy("holder")

    def form_valid(self, form: HolderForm) -> HttpResponse:
        form.instance.author = self.request.user
        logger.info(f"Holder {form.instance.holder_type} created by {form.instance.author}.")
        return super().form_valid(form)


class HolderUpdateView(BreadcrumbMixin, LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "holders.change_holder"
    model = Holder
    template_name = "holders/holder_form.html"
    form_class = HolderForm

    def get_success_url(self) -> str:
        return reverse("holder-detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form: HolderForm) -> HttpResponse:
        form.instance.author = self.request.user
        logger.info(f"Holder {form.instance.holder_type} updated by {form.instance.author}.")
        return super().form_valid(form)


class HolderDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "holders.delete_holder"
    model = Holder
    template_name = "holders/delete_confirm.html"
    success_url = "/"

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        holder = self.get_object()
        user = request.user
        logger.info(f"Holder {holder.holder_type} deleted by user {user}")
        return super().post(request, *args, **kwargs)
