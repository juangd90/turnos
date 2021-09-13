# Generated by Django 3.2.5 on 2021-09-13 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='dni',
            field=models.IntegerField(default=0, max_length=8),
        ),
        migrations.RemoveField(
            model_name='dia',
            name='horario',
        ),
        migrations.AddField(
            model_name='dia',
            name='horario',
            field=models.ManyToManyField(to='app.Hora'),
        ),
    ]