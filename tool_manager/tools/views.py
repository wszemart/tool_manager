from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from .forms import ToolForm
from .models import Tool
import logging

logger = logging.getLogger(__name__)


class ToolListView(ListView):
    model = Tool
    template_name = 'tools/tool.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        logger.info(f'Tool List View accessed by user {user}')
        return super().get(request, *args, **kwargs)


class ToolDetailView(DetailView):
    model = Tool
    template_name = 'tools/tool_detail.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        logger.info(f'Tool Detail View accessed by user {user}')
        return super().get(request, *args, **kwargs)


class ToolCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'tools.add_tool'
    model = Tool
    template_name = 'tools/tool_form.html'
    form_class = ToolForm
    success_url = reverse_lazy('tool')

    def form_valid(self, form):
        form.instance.author = self.request.user
        logger.info(f"Tool {form.instance.tool_type} created by user {form.instance.author}.")
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class ToolUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'tools.change_tool'
    model = Tool
    template_name = 'tools/tool_form.html'
    form_class = ToolForm

    def get_success_url(self):
        return reverse('tool-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        logger.info(f"Tool {form.instance.tool_type} updated by {form.instance.author}.")
        return super().form_valid(form)


class ToolDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'tools.delete_tool'
    model = Tool
    template_name = 'tools/tool_delete_confirm.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        tool = self.get_object()
        user = request.user
        logger.info(f'Tool {tool.tool_type} deleted by user {user}')
        return super().post(request, *args, **kwargs)
