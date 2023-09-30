from django.shortcuts import get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from .forms import ToolAssemblyForm, UserCommentForm, ToolAssemblySlim
from .models import ToolAssembly, UserComment
import logging

logger = logging.getLogger(__name__)


class ToolAssemblyCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'tools_assembly.add_toolassembly'
    model = ToolAssembly
    template_name = 'tools_assembly/tool_assembly_form.html'
    form_class = ToolAssemblyForm
    success_url = reverse_lazy('tool-assembly')

    def form_valid(self, form):
        form.instance.author = self.request.user
        logger.info(f"Tool assembly nr: {form.instance.tool_nr} created by user {form.instance.author}.")
        return super().form_valid(form)


class ToolAssemblyListView(ListView):
    model = ToolAssembly
    template_name = 'tools_assembly/tool_assembly.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        logger.info(f'Tool assembly List View accessed by user {user}')
        return super().get(request, *args, **kwargs)


class ToolAssemblyDetailView(DetailView):
    model = ToolAssembly
    template_name = 'tools_assembly/tool_assembly_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = UserCommentForm()
        return context

    def get(self, request, *args, **kwargs):
        tool_assembly = self.get_object()
        user = request.user
        logger.info(f'Tool assembly nr: {tool_assembly.tool_nr} Detail View accessed by user {user}')
        return super().get(request, *args, **kwargs)


class ToolAssemblyDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'tools_assembly.delete_toolassembly'
    model = ToolAssembly
    template_name = 'tools_assembly/tool_assembly_delete_confirm.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        tool_assembly = self.get_object()
        user = request.user
        logger.info(f'Tool assembly nr: {tool_assembly.tool_nr} deleted by user {user}')
        return super().post(request, *args, **kwargs)


class ToolAssemblyUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'tools_assembly.change_toolassembly'
    model = ToolAssembly
    template_name = 'tools_assembly/tool_assembly_form.html'

    def get_form_class(self):
        if self.request.user.groups.filter(name='Operator').exists():
            return ToolAssemblySlim
        else:
            return ToolAssemblyForm

    def get_success_url(self):
        return reverse('tool-assembly-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        logger.info(f"Tool assembly nr: {form.instance.tool_nr} updated by {form.instance.author}.")
        return super().form_valid(form)


class UserCommentListView(ListView):
    model = UserComment
    context_object_name = 'comments'
    ordering = ['-date_posted']
    paginate_by = 10


class ToolAssemblyAddCommentView(View):

    def post(self, request, pk):
        tool_assembly = get_object_or_404(ToolAssembly, pk=pk)
        comment_form = UserCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.toolassembly = tool_assembly
            new_comment.save()

        logger.info(f"New comment add to tool assembly nr: {tool_assembly.tool_nr} by {request.user}.")

        return redirect('tool-assembly-detail', pk=pk)
