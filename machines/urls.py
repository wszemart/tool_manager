from django.urls import path

from .views import (  # generic_pdf,
    MachineCreateView,
    MachineDeleteView,
    MachineDetailView,
    MachineUpdateView,
    generate_csv,
    home,
)

urlpatterns = [
    path("", home, name="app-home"),
    path("machine/<int:pk>/", MachineDetailView.as_view(), name="machine-detail"),
    path("machine/new/", MachineCreateView.as_view(), name="machine-create"),
    path("machine/<int:pk>/update/", MachineUpdateView.as_view(), name="machine-update"),
    path("machine/<int:pk>/delete/", MachineDeleteView.as_view(), name="machine-delete"),
    path("tools/generate-csv/", generate_csv, name="generate-csv"),
    # path("tools/generate-pdf/", generic_pdf, name="generate-pdf"),
]
