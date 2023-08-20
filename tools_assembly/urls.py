from django.contrib import admin
from django.urls import path

from .views import (HolderCreateView, HolderDeleteView, HolderDetailView,
                    HolderListView, HolderUpdateView, ToolAssemblyCreateView,
                    ToolAssemblyDeleteView, ToolAssemblyDetailView,
                    ToolAssemblyListView, ToolAssemblyUpdateView,
                    ToolCreateView, ToolDeleteView, ToolDetailView,
                    ToolListView, ToolUpdateView)

urlpatterns = [
    path('holder/', HolderListView.as_view(), name='holder'),
    path('holder/<int:pk>/', HolderDetailView.as_view(), name='holder-detail'),
    path('holder/new/', HolderCreateView.as_view(), name='holder-create'),
    path('holder/update/<int:pk>', HolderUpdateView.as_view(), name='holder-update'),
    path('holder/delete/<int:pk>', HolderDeleteView.as_view(), name='holder-delete'),
    path('tool/', ToolListView.as_view(), name='tool'),
    path('tool/<int:pk>/', ToolDetailView.as_view(), name='tool-detail'),
    path('tool/new/', ToolCreateView.as_view(), name='tool-create'),
    path('tool/update/<int:pk>', ToolUpdateView.as_view(), name='tool-update'),
    path('tool/delete/<int:pk>', ToolDeleteView.as_view(), name='tool-delete'),
    path('tool_assembly/new/', ToolAssemblyCreateView.as_view(), name='tool-assembly-create'),
    path('tool_assembly/', ToolAssemblyListView.as_view(), name='tool-assembly'),
    path('tool_assembly/<int:pk>/', ToolAssemblyDetailView.as_view(), name='tool-assembly-detail'),
    path('tool_assembly/delete/<int:pk>/', ToolAssemblyDeleteView.as_view(), name='tool-assembly-delete'),
    path('tool_assembly/update/<int:pk>/', ToolAssemblyUpdateView.as_view(), name='tool-assembly-update'),
]
