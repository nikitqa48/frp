from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone


class Organisation_adress(models.Model):
    site = models.CharField('Официальный сайт', max_length=200)
    legal_address = models.CharField('Юридический адрес', max_length=1000)
    actual_address = models.CharField('Фактический адрес', max_length=1000)
    correspondence = models.CharField('адрес корреспонденции', max_length=1000)

    class Meta:
        verbose_name = 'Адрес организации'
        verbose_name_plural = 'Адреса организаций'

    def __str__(self):
        return self.site


class Organisation(models.Model):
    short_name = models.CharField('Сокращенное имя', max_length = 200)
    full_name = models.CharField('Полное имя', max_length = 500)
    ogrn = models.CharField('ОГРН', max_length=100)
    inn = models.CharField('ИНН', max_length=100)
    kpp = models.CharField('КПП', max_length=100)
    data_registration = models.DateField('Дата гос. регистрации')
    chef = models.CharField('Руководитель организации', max_length=100)
    address = models.OneToOneField(Organisation_adress, on_delete=models.CASCADE, verbose_name='Адрес', null=True)
    contact = models.CharField('Контактное лицо', max_length=200, null=True)
    target = models.CharField('Целевое обеспечение', max_length=500, null=True)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
    
    def __str__(self):
        return self.short_name
    

class Executor(models.Model):
    name = models.CharField('Имя', max_length=100, null=False)
    description = models.TextField('Описание работ по проекту', null=True)
    type_executor = models.CharField('Тип соисполнителя', max_length=500, null=True)
    cost = models.CharField('Стоимость работ', max_length=500, null=True)

    class Meta:
        verbose_name = 'Соисполнитель'
        verbose_name_plural = 'Соисполнители'
    
    def __str__(self):
        return self.name



class Target(models.Model):
    period = models.CharField('Период запуска проекта', max_length=500)
    result = models.TextField('Результат от реализации проекта')

    class Meta:
        verbose_name = 'Цель проекта'
        verbose_name_plural = 'Цели проекта'
    
    def __str__(self):
        return self.result



class Cost(models.Model):
    budget = models.CharField('Бюджетные средства', max_length=50)
    bank = models.CharField('Банковское кредитование', max_length=50)
    own_funds = models.CharField('Собственные средства организации', max_length=50)
    other = models.CharField('Средства иных частных инвесторов', max_length=50)

    class Meta:
        verbose_name = 'Расходы'
        verbose_name_plural = 'Расходы'
    
    def __str__(self):
        return self.own_funds


class Indicator(models.Model):
    name = models.CharField('имя показателя', max_length=500)
    year = models.CharField('год', max_length=300)
    total = models.CharField('Итого', max_length=300)
    value = models.CharField('Значение', max_length=500)

    class Meta:
        verbose_name = 'Показатели'
        verbose_name_plural = 'Показатели'
    
    def __str__(self):
        return self.value

class Collateral(models.Model):
    individuals = models.TextField('Поручительства физ лиц')
    not_related = models.TextField('имущество не относ к основному обеспеч')
    guarantees = models.TextField('Гарантии банков')

    class Meta:
        verbose_name='Обеспечение'
        verbose_name_plural='Обеспечение'

class Document(models.Model):
    name = models.CharField('Название документа',max_length=100)
    document_file = models.FileField(upload_to='documents')
    data = models.DateTimeField('Дата загрузки', auto_now = True)
    type_document = models.CharField('Тип документа', max_length=50)

    class Meta:
        verbose_name = 'Документы'
        verbose_name_plural = 'Документы'

class Using(models.Model):
    name = models.TextField('Имя категории')
    salary = models.CharField('Зарплата сотрудников', max_length=100)
    services = models.TextField('Услуги 3х лиц')
    materials = models.TextField('Материалы и комплект')
    equipment = models.TextField('Оборудование')

    class Meta:
        verbose_name = 'Использование средств'
        verbose_name_plural = 'Использование средств'
 




class Project(models.Model):
    # user = models.OneToOneField(Profile, on_delete=models.CASCADE, default=0, verbose_name='Профиль')
    name = models.TextField('Название проекта')
    program = models.CharField('Программа финансовой поддержки', max_length=300)
    required_funding = models.CharField('Требуемый объем финансирования', max_length=50)
    deadline = models.DateField('Сроки возврата', null=True)
    industry = models.CharField('Отрасль промышленности', max_length=200)
    information = models.TextField('Информация о продукции')
    description = models.TextField('Описание проекта')
    result = models.TextField('Имеющийся результат по проекту')
    implementation = models.CharField('Место реализации проекта', max_length=200)
    executor = models.ForeignKey(Executor, on_delete = models.CASCADE, null=True, verbose_name='Соисполнители')
    target = models.OneToOneField(Target, related_name='target', on_delete=models.CASCADE, null=True, verbose_name="Цель")
    cost = models.OneToOneField(Cost, related_name='cost', on_delete = models.CASCADE, null=True, verbose_name='Бюджет')
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE, null=True, verbose_name='Показатели')
    сollateral = models.OneToOneField(Collateral,on_delete = models.CASCADE, null=True, verbose_name='Поручительства')
    pledges = models.TextField('Залоги')
    documents = models.ForeignKey(Document, on_delete=models.CASCADE, null=True, verbose_name='Документы')
    using_funds = models.ForeignKey(Using, on_delete=models.CASCADE, null=True, verbose_name='Расходы')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
    
    def __str__(self):
        return self.name
