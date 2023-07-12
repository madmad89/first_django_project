from django.db import models

from trainer.models import Trainer


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    description = models.TextField(max_length=300)
    active = models.BooleanField(default=True)
    start_date = models.DateField()
    end_date = models.DateField()
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True) # stocam data si ora in momentul in care adaugam studentul.
    # Data nu se mai modifica
    updated_at = models.DateTimeField(auto_now=True) # stocam data si ora in momentul in care realizam actualizari de
    # informatii pe student

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
