# Generated by Django 4.2.2 on 2023-06-20 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0002_alter_trainer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='course',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
