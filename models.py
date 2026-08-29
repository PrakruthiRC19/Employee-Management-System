from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.name