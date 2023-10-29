from django.urls import path

from .views import (
    MachineCreateView,
    MachineDeleteView,
    MachineDetailView,
    MachineUpdateView,
    generate_csv,
    generic_pdf,
    home,
)

urlpatterns = [
    path("", home, name="app-home"),
    path("machine/<int:pk>/", MachineDetailView.as_view(), name="machine-detail"),
    path("machine/new/", MachineCreateView.as_view(), name="machine-create"),
    path("machine/update/<int:pk>", MachineUpdateView.as_view(), name="machine-update"),
    path("machine/delete/<int:pk>", MachineDeleteView.as_view(), name="machine-delete"),
    path("tools/generate-csv/", generate_csv, name="generate-csv"),
    path("tools/generate-pdf/", generic_pdf, name="generate-pdf"),
]
