from django.contrib import admin
from .models import Machine
from .models import Infrastructure

# Register your models here.
admin.site.register(Machine)
admin.site.register(Infrastructure)
