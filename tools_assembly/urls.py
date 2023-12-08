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
        "tool-assembly/new/",
        ToolAssemblyCreateView.as_view(),
        name="tool-assembly-create",
    ),
    path("tool-assembly/", ToolAssemblyListView.as_view(), name="tool-assembly"),
    path(
        "tool-assembly/<int:pk>/",
        ToolAssemblyDetailView.as_view(),
        name="tool-assembly-detail",
    ),
    path(
        "tool-assembly/<int:pk>/delete/",
        ToolAssemblyDeleteView.as_view(),
        name="tool-assembly-delete",
    ),
    path(
        "tool-assembly/<int:pk>/update/",
        ToolAssemblyUpdateView.as_view(),
        name="tool-assembly-update",
    ),
    path(
        "tool-assembly/<int:pk>/add-comment/",
        ToolAssemblyAddCommentView.as_view(),
        name="add-comment",
    ),
]
