from django.db import models


# Blank = True il folosim atunci cand  vrem ca acel camp sa nu fie required

class Trainer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    course = models.CharField(max_length=40, blank=True)
    email = models.EmailField(max_length=40)
    department = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField

    updated_at = models.DateTimeField

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
