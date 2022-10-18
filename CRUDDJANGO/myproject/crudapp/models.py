from django.db import models

class Employee(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    Gender = models.CharField(max_length=50)


