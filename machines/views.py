from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import MachineForm
from .models import Machine
from django.contrib.auth.decorators import login_required
import pandas as pd
from django.http import HttpResponse
# from weasyprint import HTML
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.urls import reverse
# login_required, LoginRequiredMixin (class based view)


class BreadcrumbMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        return context

    def get_breadcrumbs(self):
        breadcrumbs = [{'title': 'Strona główna', 'url': reverse('app-home')}]

        if isinstance(self, MachineDetailView):
            machine = self.get_object()
            breadcrumbs.append({'title': machine.name, 'url': reverse('machine-detail', kwargs={'pk': machine.pk})})
        elif isinstance(self, MachineCreateView):
            breadcrumbs.append({'title': 'Utwórz nową maszynę', 'url': reverse('machine-create')})
        elif isinstance(self, MachineUpdateView):
            machine = self.get_object()
            breadcrumbs.append({'title': machine.name, 'url': reverse('machine-detail', kwargs={'pk': machine.pk})})
            breadcrumbs.append({'title': 'Aktualizuj', 'url': reverse('machine-update', kwargs={'pk': machine.pk})})

        return breadcrumbs


@login_required
def home(request):
    print("Home view accessed.")
    return render(request, 'machines/machine.html', {'title': 'Home'})


class MachineListView(BreadcrumbMixin, ListView):
    model = Machine
    template_name = 'machines/machines_list.html'


class MachineDetailView(BreadcrumbMixin, DetailView):
    model = Machine
    template_name = 'machines/machine_detail.html'


class MachineCreateView(LoginRequiredMixin, BreadcrumbMixin, CreateView):
    model = Machine
    template_name = 'machines/machine_form.html'
    form_class = MachineForm
    # fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MachineUpdateView(BreadcrumbMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Machine
    template_name = 'machines/machine_form.html'
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        machine = self.get_object()
        return self.request.user == machine.author


class MachineDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Machine
    template_name = 'machines/delete_confirm.html'
    success_url = '/'

    def test_func(self):
        machine = self.get_object()
        return self.request.user == machine.author


def generate_csv(request):
    machines = Machine.objects.all()
    data = []

    for machine in machines:
        tools = machine.tools.all()
        for tool in tools:
            data.append({
                'Nr narzędzia': tool.tool_nr,
                'Promień': tool.radius,
                'Długość całkowita': tool.total_length,
                'Długość poza oprawką': tool.outside_holder,
                'Maszyna': machine.name,
                'Typ oprawki': tool.holder.get_holder_type_display(),
                'Typ freza': tool.tool.get_tool_type_display(),
            })

    df = pd.DataFrame(data)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data-csv.csv"'
    df.to_csv(response, index=False)
    return response


# def generate_pdf(request):
#     machines = Machine.objects.all()
#     data = []
#     for machine in machines:
#         tools = machine.tools.all()
#         for tool in tools:
#             data.append({
#                 'Nr narzędzia': tool.tool_nr,
#                 'Promień': tool.radius,
#                 'Długość całkowita': tool.total_length,
#                 'Długość poza oprawką': tool.outside_holder,
#                 'Maszyna': machine.name,
#                 'Typ oprawki': tool.holder.get_holder_type_display(),
#                 'Typ freza': tool.tool.get_tool_type_display(),
#             })
#
#     context = {'data': data}
#     html_string = render_to_string('machine_detail.html', context)
#     html = HTML(string=html_string)
#     pdf_file = html.write_pdf()
#     response = HttpResponse(pdf_file, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="data-pdf.pdf"'
#     return response

