import django_filters
from student.models import Trainer


class TrainerFilters(django_filters.FilterSet):

    class Meta:
        model = Trainer
        fields = ['first_name', 'last_name', 'course']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.filters['first_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your first name'})
        self.filters['last_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your last name'})
        self.filters['course'].field.widget.attrs.update({'class': 'form-control'})
