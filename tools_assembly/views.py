from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import HolderForm, ToolForm, ToolAssemblyForm
from .models import Holder, Tool, ToolAssembly
from django.urls import reverse
from django.contrib.auth.decorators import login_required


class HolderListView(ListView):
    model = Holder
    template_name = 'tools_assembly/holder.html'


class HolderDetailView(DetailView):
    model = Holder
    template_name = 'tools_assembly/holder_detail.html'


class HolderCreateView(LoginRequiredMixin, CreateView):
    model = Holder
    template_name = 'tools_assembly/holder_form.html'
    form_class = HolderForm
    success_url = '/'


class HolderUpdateView(LoginRequiredMixin, UpdateView):
    model = Holder
    template_name = 'tools_assembly/holder_form.html'
    form_class = HolderForm

    def get_success_url(self):
        return reverse('holder-detail', kwargs={'pk': self.object.pk})

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    # def test_func(self):
    #     holder = self.get_object()
    #     return self.request.user == holder.author


class HolderDeleteView(LoginRequiredMixin, DeleteView):
    model = Holder
    template_name = 'tools_assembly/delete_confirm.html'
    success_url = '/'


class ToolListView(ListView):
    model = Tool
    template_name = 'tools_assembly/tool.html'


class ToolDetailView(DetailView):
    model = Tool
    template_name = 'tools_assembly/tool_detail.html'


class ToolCreateView(LoginRequiredMixin, CreateView):
    model = Tool
    template_name = 'tools_assembly/tool_form.html'
    form_class = ToolForm
    success_url = '/'


class ToolUpdateView(LoginRequiredMixin, UpdateView):
    model = Tool
    template_name = 'tools_assembly/tool_form.html'
    form_class = ToolForm

    def get_success_url(self):
        return reverse('tool-detail', kwargs={'pk': self.object.pk})

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    # def test_func(self):
    #     holder = self.get_object()
    #     return self.request.user == holder.author


class ToolDeleteView(LoginRequiredMixin, DeleteView):
    model = Tool
    template_name = 'tools_assembly/tool_delete_confirm.html'
    success_url = '/'


class ToolAssemblyCreateView(LoginRequiredMixin, CreateView):
    model = ToolAssembly
    template_name = 'tools_assembly/tool_assembly_form.html'
    form_class = ToolAssemblyForm
    success_url = '/'


class ToolAssemblyListView(ListView):
    model = ToolAssembly
    template_name = 'tools_assembly/tool_assembly.html'


class ToolAssemblyDetailView(DetailView):
    model = ToolAssembly
    template_name = 'tools_assembly/tool_assembly_detail.html'


class ToolAssemblyDeleteView(LoginRequiredMixin, DeleteView):
    model = ToolAssembly
    template_name = 'tools_assembly/tool_assembly_delete_confirm.html'
    success_url = '/'


class ToolAssemblyUpdateView(LoginRequiredMixin, UpdateView):
    model = ToolAssembly
    template_name = 'tools_assembly/tool_assembly_form.html'
    form_class = ToolAssemblyForm

    def get_success_url(self):
        return reverse('tool-assembly-detail', kwargs={'pk': self.object.pk})
