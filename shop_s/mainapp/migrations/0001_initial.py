# Generated by Django 3.2 on 2021-04-23 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order_material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=255, verbose_name='Наименование материала')),
                ('unit', models.CharField(max_length=5, verbose_name='Единица измерения')),
                ('objec', models.CharField(max_length=255, verbose_name='Объект')),
                ('persona_1', models.PositiveSmallIntegerField(verbose_name='Работник 1')),
            ],
        ),
    ]
