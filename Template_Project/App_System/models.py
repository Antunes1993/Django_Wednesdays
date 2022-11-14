from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Equipment(models.Model):
    tag = models.CharField('Equipment Tag', max_length=120)
    address = models.CharField(max_length=300)
    type = models.CharField('Type', max_length=60)    

    def __str__(self):
        return self.tag


class Employee(models.Model):
    first_name = models.CharField('First Name', max_length=120)
    last_name = models.CharField('Last Name', max_length=120)
    email = models.EmailField('Email Address')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Maintenance(models.Model):
    name = models.CharField('Maintenance name', max_length=120)
    maintenance_identification = models.IntegerField('Maintenance ID', max_length=20)
    maintenance_date = models.DateTimeField()
    equipment = models.ForeignKey(Equipment, blank=True, null=True, on_delete=models.CASCADE)
    
    #Setting a system user as a manager. 
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(Employee, blank=True)

    def __str__(self):
        return self.name


