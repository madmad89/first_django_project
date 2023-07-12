import django_filters
from django import forms
from student.models import Student


class StudentFilters(django_filters.FilterSet):
    list_of_students = [((student.first_name, student.first_name.upper())) for student in
                        Student.objects.filter(active=True)]

    first_name = django_filters.ChoiceFilter(choices=list(set(list_of_students)))

    # first_name = django_filters.CharFilter(lookup_expr='icontains', label='First name')
    last_name = django_filters.CharFilter(lookup_expr='icontains', label='Last name')

    start_date_gte = django_filters.DateFilter(field_name='start_date', lookup_expr='gte', label='From',
                                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    start_date_lte = django_filters.DateFilter(field_name='start_date', lookup_expr='lte', label='To',
                                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'active', 'start_date_gte', 'start_date_lte', 'trainer']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.filters['first_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your first name'})
        self.filters['last_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your first name'})
        self.filters['active'].field.widget.attrs.update({'class': 'form-select'})
        self.filters['trainer'].field.widget.attrs.update({'class': 'form-select'})
