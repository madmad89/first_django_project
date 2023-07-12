import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from student.filters import StudentFilters
from student.forms import StudentForm, StudentUpdateForm
from student.models import Student
from trainer.models import Trainer


# CreateView-> il folosim pentru a adauga si salva date in baza de date pe baza unui formular


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'student/create_student.html'
    model = Student
    # SuccessMessageMixin se folosescte atunci cand avem data intrun table si vrem sa ne afoseze un mesaj.
    # fields = '__all__' #daca vrem sa nu mai definim noi ce filds vrem sa apra pe pagina html
    # fields = ['first_name', 'last_name', 'age', 'email', 'description',
    #           'active', 'start_date', 'end_date', 'trainer']
    # fields s-a mutat in fisierul forms

    form_class = StudentForm
    success_url = reverse_lazy('list-of-students')
    success_message = 'Felicitate! {f_name} {l_name} a fost adaugat cu success!'
    permission_required = 'student.add_student'

    def get_success_message(self, cleaned_data):
        return self.success_message.format(f_name=self.object.first_name, l_name=self.object.last_name)


# ListView -> Afisa informatii dintr-o tabela (student_student)

class StudentListView(LoginRequiredMixin, PermissionRequiredMixin,  ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'all_students'  # este o variabila de context. Student.object.all()
    permission_required = 'student.view_list_of_students'

    def get_queryset(self):
        return Student.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        now = datetime.datetime.now()
        context['current_date'] = now

        trainers = Trainer.objects.all()
        context['get_all_trainers'] = trainers

        # Search

        my_filters = StudentFilters(self.request.GET, queryset=Student.objects.filter(active=True))
        get_all_students = my_filters.qs

        context['all_students'] = get_all_students
        context['form_filters'] = my_filters.form

        return context


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('list-of-students')


# DeleteView il folosim pentru a sterge o intrare din tablela student_student


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list-of-students')


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'student/details_student.html'
    model = Student
