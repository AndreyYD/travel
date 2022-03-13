# Generated by Django 3.2 on 2022-03-12 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='citymodel',
            options={'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterField(
            model_name='citymodel',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='City'),
        ),
    ]