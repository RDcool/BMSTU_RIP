# Generated by Django 3.2.9 on 2021-11-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('photo', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('topping', models.CharField(max_length=200, verbose_name='Состав')),
                ('diameter', models.IntegerField(default=23, verbose_name='Диаметр пиццы в см')),
            ],
            options={
                'verbose_name': 'Пицца',
                'verbose_name_plural': 'Пиццы',
            },
        ),
    ]