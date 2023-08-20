from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import MachineForm
from .models import Machine
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# login_required, LoginRequiredMixin (class based view)


@login_required
def home(request):
    print("Home view accessed.")
    return render(request, 'machines/machine.html', {'title': 'Home'})


class MachineListView(ListView):
    model = Machine
    template_name = 'machines/machines_list.html'


class MachineDetailView(DetailView):
    model = Machine
    template_name = 'machines/machine_detail.html'


class MachineCreateView(LoginRequiredMixin, CreateView):
    model = Machine
    template_name = 'machines/machine_form.html'
    form_class = MachineForm
    # fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MachineUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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
