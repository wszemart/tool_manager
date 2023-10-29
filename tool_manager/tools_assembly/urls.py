from django.urls import path

from .views import (
    ToolAssemblyAddCommentView,
    ToolAssemblyCreateView,
    ToolAssemblyDeleteView,
    ToolAssemblyDetailView,
    ToolAssemblyListView,
    ToolAssemblyUpdateView,
)

urlpatterns = [
    path(
        "tool_assembly/new/",
        ToolAssemblyCreateView.as_view(),
        name="tool-assembly-create",
    ),
    path("tool_assembly/", ToolAssemblyListView.as_view(), name="tool-assembly"),
    path(
        "tool_assembly/<int:pk>/",
        ToolAssemblyDetailView.as_view(),
        name="tool-assembly-detail",
    ),
    path(
        "tool_assembly/delete/<int:pk>/",
        ToolAssemblyDeleteView.as_view(),
        name="tool-assembly-delete",
    ),
    path(
        "tool_assembly/update/<int:pk>/",
        ToolAssemblyUpdateView.as_view(),
        name="tool-assembly-update",
    ),
    path(
        "tool-assembly/<int:pk>/add-comment/",
        ToolAssemblyAddCommentView.as_view(),
        name="add-comment",
    ),
]
