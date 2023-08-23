from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import HolderForm, ToolForm, ToolAssemblyForm, UserCommentForm
from .models import Holder, Tool, ToolAssembly, UserComment
from django.urls import reverse
from django.contrib.auth.decorators import login_required


class BreadcrumbMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        return context

    def get_breadcrumbs(self):
        breadcrumbs = [{'title': 'Strona główna', 'url': reverse('app-home')}]

        if isinstance(self, HolderListView):
            breadcrumbs.append({'title': 'Lista oprawek', 'url': reverse('holder')})

        elif isinstance(self, HolderDetailView) or isinstance(self, HolderUpdateView):
            holder = self.get_object()
            breadcrumbs.append({'title': 'Lista oprawek', 'url': reverse('holder')})
            breadcrumbs.append(
                {'title': holder.get_holder_type_display, 'url': reverse('holder-detail', kwargs={'pk': holder.pk})})
            if isinstance(self, HolderUpdateView):
                breadcrumbs.append({'title': 'Aktualizuj', 'url': reverse('holder-update', kwargs={'pk': holder.pk})})

        elif isinstance(self, HolderCreateView):
            breadcrumbs.append({'title': 'Lista oprawek', 'url': reverse('holder')})
            breadcrumbs.append({'title': 'Utwórz nową oprawkę', 'url': reverse('holder-create')})

        elif isinstance(self, ToolListView):
            breadcrumbs.append({'title': 'Lista frezów', 'url': reverse('tool')})

        elif isinstance(self, ToolDetailView) or isinstance(self, ToolUpdateView):
            tool = self.get_object()
            breadcrumbs.append({'title': 'Lista frezów', 'url': reverse('tool')})
            breadcrumbs.append({'title': tool.get_tool_type_display, 'url': reverse('tool-detail', kwargs={'pk': tool.pk})})
            if isinstance(self, ToolUpdateView):
                breadcrumbs.append({'title': 'Aktualizuj', 'url': reverse('tool-update', kwargs={'pk': tool.pk})})

        elif isinstance(self, ToolCreateView):
            breadcrumbs.append({'title': 'Lista frezów', 'url': reverse('tool')})
            breadcrumbs.append({'title': 'Utwórz nowy frez', 'url': reverse('tool-create')})

        elif isinstance(self, ToolAssemblyListView):
            breadcrumbs.append({'title': 'Lista narzędzi', 'url': reverse('tool-assembly')})

        elif isinstance(self, ToolAssemblyDetailView) or isinstance(self, ToolAssemblyUpdateView):
            tool_assembly = self.get_object()
            breadcrumbs.append({'title': 'Lista narzędzi', 'url': reverse('tool-assembly')})
            breadcrumbs.append({'title': f'T{tool_assembly.tool_nr} R{tool_assembly.radius} {tool_assembly.tool.get_tool_type_display()}', 'url': reverse('tool-assembly-detail', kwargs={'pk': tool_assembly.pk})})
            if isinstance(self, ToolAssemblyUpdateView):
                breadcrumbs.append({'title': 'Aktualizuj', 'url': reverse('tool-assembly-update', kwargs={'pk': tool_assembly.pk})})
        elif isinstance(self, ToolAssemblyCreateView):
            breadcrumbs.append({'title': 'Lista narzędzi', 'url': reverse('tool-assembly')})
            breadcrumbs.append({'title': 'Utwórz nowe narzędzie', 'url': reverse('tool-assembly-create')})

        return breadcrumbs


class HolderListView(BreadcrumbMixin, ListView):
    model = Holder
    template_name = 'tools_assembly/holder.html'


class HolderDetailView(BreadcrumbMixin, DetailView):
    model = Holder
    template_name = 'tools_assembly/holder_detail.html'


class HolderCreateView(BreadcrumbMixin, LoginRequiredMixin, CreateView):
    model = Holder
    template_name = 'tools_assembly/holder_form.html'
    form_class = HolderForm
    success_url = '/'


class HolderUpdateView(BreadcrumbMixin, LoginRequiredMixin, UpdateView):
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


class ToolListView(BreadcrumbMixin, ListView):
    model = Tool
    template_name = 'tools_assembly/tool.html'


class ToolDetailView(BreadcrumbMixin, DetailView):
    model = Tool
    template_name = 'tools_assembly/tool_detail.html'


class ToolCreateView(BreadcrumbMixin, LoginRequiredMixin, CreateView):
    model = Tool
    template_name = 'tools_assembly/tool_form.html'
    form_class = ToolForm
    success_url = '/'


class ToolUpdateView(BreadcrumbMixin, LoginRequiredMixin, UpdateView):
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


class ToolAssemblyCreateView(BreadcrumbMixin, LoginRequiredMixin, CreateView):
    model = ToolAssembly
    template_name = 'tools_assembly/tool_assembly_form.html'
    form_class = ToolAssemblyForm
    success_url = '/'


class ToolAssemblyListView(BreadcrumbMixin, ListView):
    model = ToolAssembly
    template_name = 'tools_assembly/tool_assembly.html'


class ToolAssemblyDetailView(BreadcrumbMixin, DetailView):
    model = ToolAssembly
    template_name = 'tools_assembly/tool_assembly_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = UserCommentForm()
        return context


class ToolAssemblyDeleteView(LoginRequiredMixin, DeleteView):
    model = ToolAssembly
    template_name = 'tools_assembly/tool_assembly_delete_confirm.html'
    success_url = '/'


class ToolAssemblyUpdateView(BreadcrumbMixin, LoginRequiredMixin, UpdateView):
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
        if comment_form.is_valid():
            print(comment_form.errors)
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.toolassembly = tool_assembly
            new_comment.save()
        return redirect('tool-assembly-detail', pk=pk)
