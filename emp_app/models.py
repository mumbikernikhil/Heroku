from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    position = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s %s" %(self.first_name, self.last_name, self.email)

class Designation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name