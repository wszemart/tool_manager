from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.contrib.auth.models import User
from notifications.models import UserNotification, Notification


from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import HolderForm, ToolForm, ToolAssemblyForm, UserCommentForm
from .models import Holder, Tool, ToolAssembly, UserComment
from .mixins import BreadcrumbMixin

# BREADCRUMB_CONFIG = {
#     HolderListView: [
#         {'title': 'Lista oprawek', 'url': reverse('holder')}
#     ],
#
# } # TODO file breadcrum_config.py
# # BreadcrumbMixin -> mixins.py



class HolderListView(ListView, BreadcrumbMixin):
    model = Holder
    template_name = 'tools_assembly/holder.html'


class HolderDetailView(DetailView, BreadcrumbMixin):
    model = Holder
    template_name = 'tools_assembly/holder_detail.html'


class HolderCreateView(LoginRequiredMixin, CreateView, BreadcrumbMixin):
    model = Holder
    template_name = 'tools_assembly/holder_form.html'
    form_class = HolderForm
    success_url = '/'


class HolderUpdateView(LoginRequiredMixin, UpdateView, BreadcrumbMixin):
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


class HolderDeleteView(LoginRequiredMixin, DeleteView, BreadcrumbMixin):
    model = Holder
    template_name = 'tools_assembly/delete_confirm.html'
    success_url = '/'


class ToolListView(ListView, BreadcrumbMixin):
    model = Tool
    template_name = 'tools_assembly/tool.html'


class ToolDetailView(DetailView, BreadcrumbMixin):
    model = Tool
    template_name = 'tools_assembly/tool_detail.html'


class ToolCreateView(LoginRequiredMixin, CreateView, BreadcrumbMixin):
    model = Tool
    template_name = 'tools_assembly/tool_form.html'
    form_class = ToolForm
    success_url = '/'


class ToolUpdateView(LoginRequiredMixin, UpdateView, BreadcrumbMixin):
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


class ToolDeleteView(LoginRequiredMixin, DeleteView, BreadcrumbMixin):
    model = Tool
    template_name = 'tools_assembly/tool_delete_confirm.html'
    success_url = '/'


class ToolAssemblyCreateView(LoginRequiredMixin, CreateView, BreadcrumbMixin):
    model = ToolAssembly
    template_name = 'tools_assembly/tool_assembly_form.html'
    form_class = ToolAssemblyForm
    success_url = '/'


class ToolAssemblyListView(ListView, BreadcrumbMixin):
    model = ToolAssembly
    template_name = 'tools_assembly/tool_assembly.html'


class ToolAssemblyDetailView(DetailView, BreadcrumbMixin):
    model = ToolAssembly
    template_name = 'tools_assembly/tool_assembly_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = UserCommentForm()
        return context


class ToolAssemblyDeleteView(LoginRequiredMixin, DeleteView, BreadcrumbMixin):
    model = ToolAssembly
    template_name = 'tools_assembly/tool_assembly_delete_confirm.html'
    success_url = '/'


class ToolAssemblyUpdateView(LoginRequiredMixin, UpdateView, BreadcrumbMixin):
    model = ToolAssembly
    template_name = 'tools_assembly/tool_assembly_form.html'
    form_class = ToolAssemblyForm

    def get_success_url(self):
        return reverse('tool-assembly-detail', kwargs={'pk': self.object.pk})


class UserCommentListView(ListView):
    model = UserComment
    context_object_name = 'comments'
    ordering = ['-date_posted']
    paginate_by = 10


class ToolAssemblyAddCommentView(View):
    def post(self, request, pk):
        tool_assembly = get_object_or_404(ToolAssembly, pk=pk)
        comment_form = UserCommentForm(request.POST)
        print('before comment')
        if comment_form.is_valid():
            print(comment_form.errors)
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.toolassembly = tool_assembly
            new_comment.save()

            print('after comment and notification')

        print('view from tool asembly')

        return redirect('tool-assembly-detail', pk=pk)
