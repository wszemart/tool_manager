from django.contrib import admin
from django.urls import path
from .views import MachineDetailView, home, MachineCreateView, MachineDeleteView, MachineUpdateView, generate_csv
urlpatterns = [
    path('', home, name='app-home'),
    path('machine/<int:pk>/', MachineDetailView.as_view(), name='machine-detail'),
    path('machine/new/', MachineCreateView.as_view(), name='machine-create'),
    path('machine/update/<int:pk>', MachineUpdateView.as_view(), name='machine-update'),
    path('machine/delete/<int:pk>', MachineDeleteView.as_view(), name='machine-delete'),
    path('tools/generate-csv/', generate_csv, name='generate-csv'),
    # path('tools/generate-pdf/', generate_pdf, name='generate-pdf'),
]

