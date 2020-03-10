from django.contrib import admin
from .models import *
# Register your models here
@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ['phone', 'organisation', 'user']
