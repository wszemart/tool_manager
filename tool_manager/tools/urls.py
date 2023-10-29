from django.urls import path

from .views import ToolCreateView, ToolDeleteView, ToolDetailView, ToolListView, ToolUpdateView

urlpatterns = [
    path("tool/", ToolListView.as_view(), name="tool"),
    path("tool/<int:pk>/", ToolDetailView.as_view(), name="tool-detail"),
    path("tool/new/", ToolCreateView.as_view(), name="tool-create"),
    path("tool/<int:pk>/update/", ToolUpdateView.as_view(), name="tool-update"),
    path("tool/<int:pk>/delete/", ToolDeleteView.as_view(), name="tool-delete"),
]
