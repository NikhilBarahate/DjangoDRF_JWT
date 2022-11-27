from django.db import models

# Create your models here.
class Employee(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    addr = models.CharField(max_length=200)
    sal = models.FloatField()

    def __str__(self):
        return self.name
    