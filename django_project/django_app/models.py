from django.db import models
from django.contrib import admin


# Create your models here.
class Person(models.Model):
    Name = models.CharField(max_length=20)
    Age = models.IntegerField()
    Education = models.CharField(max_length=20)
    Height = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.Name


class repr(admin.ModelAdmin):
    list_display = ("Name", "Age", "Education", "Height")
