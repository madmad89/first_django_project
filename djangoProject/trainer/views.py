import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from trainer.filters import TrainerFilters
from trainer.forms import TrainerForm, TrainerUpdateForm
from trainer.models import Trainer


class TrainerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'trainer/create_trainer.html'
    model = Trainer
    # fields = '__all__'
    # fields = ['first_name', 'last_name', 'course', 'email', 'department',
    #           'active']
    # all fields s au mutat in fisierul forms

    form_class = TrainerForm
    success_url = reverse_lazy('home_page')
    permission_required = 'trainer.add_trainer'


class TrainerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = "trainer/list_of_trainers.html"
    model = Trainer
    context_object_name = "all_trainers"
    permission_required = 'trainer.can_view_list_of_trainer'

    def get_queryset(self):
        return Trainer.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)



        # Search

        my_filters = TrainerFilters(self.request.GET, queryset=Trainer.objects.filter(active=True))
        get_all_trainers = my_filters.qs

        context['all_trainers'] = get_all_trainers
        context['form_filters'] = my_filters.form

        return context


class TrainerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'trainer/update_trainer.html'
    model = Trainer
    form_class = TrainerUpdateForm
    success_url = reverse_lazy('list-of-trainers')
    permission_required = 'trainer.change_trainer'


class TrainerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'trainer/delete_trainer.html'
    model = Trainer
    success_url = reverse_lazy('list-of-trainers')
    permission_required = 'trainer.delete_trainer'


class TrainerDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'trainer/details_trainer.html'
    model = Trainer
    permission_required = 'trainer.view_trainer'
