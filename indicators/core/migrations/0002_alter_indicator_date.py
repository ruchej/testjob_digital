# Generated by Django 4.0.6 on 2022-08-03 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='date',
            field=models.DateField(verbose_name='Дата добавления данных'),
        ),
    ]
