# Generated by Django 4.1.3 on 2022-11-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_pricing_in_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=45, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=225, unique=True),
        ),
    ]
