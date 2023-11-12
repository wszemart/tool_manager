import logging
from typing import Dict, List, Union

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .forms import ToolForm
from .models import Tool

Breadcrumb = Dict[str, Union[str, str]]

logger = logging.getLogger(__name__)


class BreadcrumbMixin:
    def get_context_data(self, **kwargs) -> Dict[str, Union[str, List[Breadcrumb]]]:
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = self.get_breadcrumbs()
        return context

    def get_breadcrumbs(self) -> List[Breadcrumb]:
        breadcrumbs = [{"title": "Strona główna", "url": reverse("app-home")}]

        if isinstance(self, ToolListView):
            breadcrumbs.append({"title": "Tabela frezów", "url": reverse("tool")})
        elif isinstance(self, ToolDetailView):
            tool = self.get_object()
            breadcrumbs.append({"title": "Tabela frezów", "url": reverse("tool")})
            breadcrumbs.append(
                {
                    "title": f"Frez: {tool.get_tool_type_display()}, FI: {tool.D1}",
                    "url": reverse("tool-detail", kwargs={"pk": tool.pk}),
                }
            )
        elif isinstance(self, ToolCreateView):
            breadcrumbs.append({"title": "Utwórz nowy frez", "url": reverse("tool-create")})
        elif isinstance(self, ToolUpdateView):
            tool = self.get_object()
            breadcrumbs.append({"title": "Tabela frezów", "url": reverse("tool")})
            breadcrumbs.append(
                {
                    "title": "Aktualizuj frez",
                    "url": reverse("tool-update", kwargs={"pk": tool.pk}),
                }
            )

        return breadcrumbs


class ToolListView(BreadcrumbMixin, ListView):
    model = Tool
    template_name = "tools/tool.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        logger.info(f"Tool List View accessed by user {request.user}")
        return super().get(request, *args, **kwargs)


class ToolDetailView(BreadcrumbMixin, DetailView):
    model = Tool
    template_name = "tools/tool_detail.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        user = request.user
        logger.info(f"Tool Detail View accessed by user {user}")
        return super().get(request, *args, **kwargs)


class ToolCreateView(BreadcrumbMixin, LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "tools.add_tool"
    model = Tool
    template_name = "tools/tool_form.html"
    form_class = ToolForm
    success_url = reverse_lazy("tool")

    def form_valid(self, form: ToolForm) -> HttpResponse:
        form.instance.author = self.request.user
        logger.info(f"Tool {form.instance.tool_type} created by user {form.instance.author}.")
        return super().form_valid(form)

    def form_invalid(self, form: ToolForm) -> HttpResponse:
        print(form.errors)
        return super().form_invalid(form)


class ToolUpdateView(BreadcrumbMixin, LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "tools.change_tool"
    model = Tool
    template_name = "tools/tool_form.html"
    form_class = ToolForm

    def get_success_url(self) -> str:
        return reverse("tool-detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form: ToolForm) -> HttpResponse:
        form.instance.author = self.request.user
        logger.info(f"Tool {form.instance.tool_type} updated by {form.instance.author}.")
        return super().form_valid(form)


class ToolDeleteView(BreadcrumbMixin, LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "tools.delete_tool"
    model = Tool
    template_name = "tools/tool_delete_confirm.html"
    success_url = "/"

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        tool = self.get_object()
        logger.info(f"Tool {tool.tool_type} deleted by user {request.user}")
        return super().post(request, *args, **kwargs)
