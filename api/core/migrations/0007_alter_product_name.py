# Generated by Django 4.1.3 on 2022-11-18 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_category_name_alter_order_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=225),
        ),
    ]
