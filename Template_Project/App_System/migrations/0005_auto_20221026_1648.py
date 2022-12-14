# Generated by Django 3.2.5 on 2022-10-26 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App_System', '0004_rename_clubuser_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=120, verbose_name='Equipment Tag')),
                ('address', models.CharField(max_length=300)),
                ('type', models.CharField(max_length=60, verbose_name='Type')),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Maintenance name')),
                ('maintenance_identification', models.IntegerField(max_length=20, verbose_name='Maintenance ID')),
                ('maintenance_date', models.DateTimeField()),
                ('description', models.TextField(blank=True)),
                ('attendees', models.ManyToManyField(blank=True, to='App_System.Employee')),
                ('equipment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App_System.equipment')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Venue',
        ),
    ]
