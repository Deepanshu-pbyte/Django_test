from django.contrib import admin
from .models import Person, repr

# Register your models here.

admin.site.register(Person, repr)
