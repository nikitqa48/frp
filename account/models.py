from django.db import models
from project .models import *
from django.contrib.auth.models import User, Group
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  verbose_name='Пользователь', null=False, default=0)
    organisation = models.OneToOneField(Organisation, on_delete=models.CASCADE, null=True, verbose_name='Организация')
    phone = models.CharField('Телефон', max_length=20)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

