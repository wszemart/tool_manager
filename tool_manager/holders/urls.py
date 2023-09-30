from django.urls import path
from .views import (HolderCreateView, HolderDeleteView, HolderDetailView,
                    HolderListView, HolderUpdateView)

urlpatterns = [
    path('holder/', HolderListView.as_view(), name='holder'),
    path('holder/<int:pk>/', HolderDetailView.as_view(), name='holder-detail'),
    path('holder/new/', HolderCreateView.as_view(), name='holder-create'),
    path('holder/update/<int:pk>', HolderUpdateView.as_view(), name='holder-update'),
    path('holder/delete/<int:pk>', HolderDeleteView.as_view(), name='holder-delete'),
]
