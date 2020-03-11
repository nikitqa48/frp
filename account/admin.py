from django.contrib import admin
from .models import *
# Register your models here
@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = [ 'user', 'phone', 'organisation']

@admin.register(Organisation)
class AdminOrganisation(admin.ModelAdmin):
    list_display = ['full_name', 'short_name', 'inn', 'kpp', 'ogrn', 'data_registration', 'chef', 'contact', 'target', 'address']

@admin.register(Organisation_adress)
class AdminnAddress(admin.ModelAdmin):
    list_display = ['site']