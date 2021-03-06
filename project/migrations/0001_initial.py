# Generated by Django 2.2.6 on 2020-03-10 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collateral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('individuals', models.TextField(verbose_name='Поручительства физ лиц')),
                ('not_related', models.TextField(verbose_name='имущество не относ к основному обеспеч')),
                ('guarantees', models.TextField(verbose_name='Гарантии банков')),
            ],
            options={
                'verbose_name': 'Обеспечение',
                'verbose_name_plural': 'Обеспечение',
            },
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.CharField(max_length=50, verbose_name='Бюджетные средства')),
                ('bank', models.CharField(max_length=50, verbose_name='Банковское кредитование')),
                ('own_funds', models.CharField(max_length=50, verbose_name='Собственные средства организации')),
                ('other', models.CharField(max_length=50, verbose_name='Средства иных частных инвесторов')),
            ],
            options={
                'verbose_name': 'Расходы',
                'verbose_name_plural': 'Расходы',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название документа')),
                ('document_file', models.FileField(upload_to='documents')),
                ('data', models.DateTimeField(auto_now=True, verbose_name='Дата загрузки')),
                ('type_document', models.CharField(max_length=50, verbose_name='Тип документа')),
            ],
            options={
                'verbose_name': 'Документы',
                'verbose_name_plural': 'Документы',
            },
        ),
        migrations.CreateModel(
            name='Executor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('description', models.TextField(null=True, verbose_name='Описание работ по проекту')),
                ('type_executor', models.CharField(max_length=500, null=True, verbose_name='Тип соисполнителя')),
                ('cost', models.CharField(max_length=500, null=True, verbose_name='Стоимость работ')),
            ],
            options={
                'verbose_name': 'Соисполнитель',
                'verbose_name_plural': 'Соисполнители',
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='имя показателя')),
                ('year', models.CharField(max_length=300, verbose_name='год')),
                ('total', models.CharField(max_length=300, verbose_name='Итого')),
                ('value', models.CharField(max_length=500, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Показатели',
                'verbose_name_plural': 'Показатели',
            },
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=200, verbose_name='Сокращенное имя')),
                ('full_name', models.CharField(max_length=500, verbose_name='Полное имя')),
                ('ogrn', models.CharField(max_length=100, verbose_name='ОГРН')),
                ('inn', models.CharField(max_length=100, verbose_name='ИНН')),
                ('kpp', models.CharField(max_length=100, verbose_name='КПП')),
                ('data_registration', models.DateField(verbose_name='Дата гос. регистрации')),
                ('chef', models.CharField(max_length=100, verbose_name='Руководитель организации')),
                ('contact', models.CharField(max_length=200, null=True, verbose_name='Контактное лицо')),
                ('target', models.CharField(max_length=500, null=True, verbose_name='Целевое обеспечение')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
        migrations.CreateModel(
            name='Organisation_adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=200, verbose_name='Официальный сайт')),
                ('legal_address', models.CharField(max_length=1000, verbose_name='Юридический адрес')),
                ('actual_address', models.CharField(max_length=1000, verbose_name='Фактический адрес')),
                ('correspondence', models.CharField(max_length=1000, verbose_name='адрес корреспонденции')),
            ],
            options={
                'verbose_name': 'Адрес организации',
                'verbose_name_plural': 'Адреса организаций',
            },
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=500, verbose_name='Период запуска проекта')),
                ('result', models.TextField(verbose_name='Результат от реализации проекта')),
            ],
            options={
                'verbose_name': 'Цель проекта',
                'verbose_name_plural': 'Цели проекта',
            },
        ),
        migrations.CreateModel(
            name='Using',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Имя категории')),
                ('salary', models.CharField(max_length=100, verbose_name='Зарплата сотрудников')),
                ('services', models.TextField(verbose_name='Услуги 3х лиц')),
                ('materials', models.TextField(verbose_name='Материалы и комплект')),
                ('equipment', models.TextField(verbose_name='Оборудование')),
            ],
            options={
                'verbose_name': 'Использование средств',
                'verbose_name_plural': 'Использование средств',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название проекта')),
                ('program', models.CharField(max_length=300, verbose_name='Программа финансовой поддержки')),
                ('required_funding', models.CharField(max_length=50, verbose_name='Требуемый объем финансирования')),
                ('deadline', models.DateField(null=True, verbose_name='Сроки возврата')),
                ('industry', models.CharField(max_length=200, verbose_name='Отрасль промышленности')),
                ('information', models.TextField(verbose_name='Информация о продукции')),
                ('description', models.TextField(verbose_name='Описание проекта')),
                ('result', models.TextField(verbose_name='Имеющийся результат по проекту')),
                ('implementation', models.CharField(max_length=200, verbose_name='Место реализации проекта')),
                ('pledges', models.TextField(verbose_name='Залоги')),
                ('cost', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cost', to='project.Cost', verbose_name='Бюджет')),
                ('documents', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Document', verbose_name='Документы')),
                ('executor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Executor', verbose_name='Соисполнители')),
                ('indicator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Indicator', verbose_name='Показатели')),
                ('target', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='target', to='project.Target', verbose_name='Цель')),
                ('using_funds', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Using', verbose_name='Расходы')),
                ('сollateral', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Collateral', verbose_name='Поручительства')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('organisation', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Organisation', verbose_name='Организация')),
                ('user', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.AddField(
            model_name='organisation',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Organisation_adress', verbose_name='Адрес'),
        ),
    ]
