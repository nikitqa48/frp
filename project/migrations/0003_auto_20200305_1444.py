# Generated by Django 2.2.6 on 2020-03-05 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20200305_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cost',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cost', to='project.Cost', verbose_name='Бюджет'),
        ),
        migrations.AlterField(
            model_name='project',
            name='documents',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Document', verbose_name='Документы'),
        ),
        migrations.AlterField(
            model_name='project',
            name='executor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Executor', verbose_name='Соисполнители'),
        ),
        migrations.AlterField(
            model_name='project',
            name='indicator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Indicator', verbose_name='Показатели'),
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='project.Profile', verbose_name='Профиль'),
        ),
        migrations.AlterField(
            model_name='project',
            name='using_funds',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Using', verbose_name='Расходы'),
        ),
        migrations.AlterField(
            model_name='project',
            name='сollateral',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Collateral', verbose_name='Поручительства'),
        ),
    ]