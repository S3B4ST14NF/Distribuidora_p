# Generated by Django 3.2.7 on 2023-09-10 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0005_rename_categoria_category_rename_project_producto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(),
        ),
    ]
