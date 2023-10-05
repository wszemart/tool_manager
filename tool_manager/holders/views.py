from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from .forms import HolderForm
from .models import Holder
import logging

logger = logging.getLogger(__name__)


class HolderListView(ListView):
    model = Holder
    template_name = 'holders/holder.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        logger.info(f'Holder List View accessed by user {user}')
        return super().get(request, *args, **kwargs)


class HolderDetailView(DetailView):
    model = Holder
    template_name = 'holders/holder_detail.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        logger.info(f'Holder Detail View accessed by user {user}')
        return super().get(request, *args, **kwargs)


class HolderCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'holders.add_holder'
    model = Holder
    template_name = 'holders/holder_form.html'
    form_class = HolderForm
    success_url = reverse_lazy('holder')

    def form_valid(self, form):
        form.instance.author = self.request.user
        logger.info(f"Holder {form.instance.holder_type} created by {form.instance.author}.")
        return super().form_valid(form)


class HolderUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'holders.change_holder'
    model = Holder
    template_name = 'holders/holder_form.html'
    form_class = HolderForm

    def get_success_url(self):
        return reverse('holder-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        logger.info(f"Holder {form.instance.holder_type} updated by {form.instance.author}.")
        return super().form_valid(form)


class HolderDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'holders.delete_holder'
    model = Holder
    template_name = 'holders/delete_confirm.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        holder = self.get_object()
        user = request.user
        logger.info(f'Holder {holder.holder_type} deleted by user {user}')
        return super().post(request, *args, **kwargs)
