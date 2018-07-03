# Generated by Django 2.0.6 on 2018-06-19 21:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20180619_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childsdetail',
            name='type_diagnostic',
        ),
        migrations.AlterField(
            model_name='childs',
            name='age_breastfeeding',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Edad en que se abandona la lactancia materna'),
        ),
    ]