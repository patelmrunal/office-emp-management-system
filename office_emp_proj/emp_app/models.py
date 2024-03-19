from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100)
   
    def __str__(self):
        return self.name

class Employee(models.Model):
    firstname = models.CharField(max_length=6)
    lastname = models.CharField(max_length=10)
    dept = models.CharField(max_length=20)
    salary = models.IntegerField(default=0)
    bouns = models.IntegerField(default=0)
    role = models.CharField(max_length=20)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return "%s %s %s" %(self.firstname, self.lastname, self.phone)