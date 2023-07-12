from django.db import models

# Create your models here.


class Book(models.Model):
    autor = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'