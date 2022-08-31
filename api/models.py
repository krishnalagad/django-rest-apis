import email
from turtle import position
from django.db import models

# Create your models here.

# creating company Model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100, choices = (('IT', 'IT'), ('Non IT', 'Non IT'), ('Other', 'Other')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ", " + self.location

# employee model
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    about = models.TextField()
    position = models.CharField(max_length=50, choices = (('Manager', 'Manager'), ('Developer', 'Developer'), ('Team Lead', 'Team Lead')))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

