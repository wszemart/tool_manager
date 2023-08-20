from django.contrib import admin
from django.urls import path
from .views import MachineDetailView, MachineListView, home, MachineCreateView, MachineDeleteView, MachineUpdateView


urlpatterns = [
    path('', home, name='app-home'),
    path('machine/<int:pk>/', MachineDetailView.as_view(), name='machine-detail'),
    path('machine/new/', MachineCreateView.as_view(), name='machine-create'),
    path('machine/update/<int:pk>', MachineUpdateView.as_view(), name='machine-update'),
    path('machine/delete/<int:pk>', MachineDeleteView.as_view(), name='machine-delete')
]

