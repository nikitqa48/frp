from django.contrib import admin
from project.models import *
# Register your models here
@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone', 'organisation', 'last_name', 'first_name']
