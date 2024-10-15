from django.contrib import admin
# Register your models here.

from .models import Infrastructure, Panne

admin.site.register(Infrastructure)
admin.site.register(Panne)
