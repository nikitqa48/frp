from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    list_display = ['name', 'program', 'required_funding','deadline','industry',
    'information','description','result','implementation',
    'executor','target','cost','indicator','сollateral',
    'pledges','documents','using_funds','executor'
    ]
@admin.register(Executor)
class AdminExecutor(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Cost)
class AdminCost(admin.ModelAdmin):
    list_display = ['bank']