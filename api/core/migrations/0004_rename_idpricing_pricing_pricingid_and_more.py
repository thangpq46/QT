# Generated by Django 4.1.3 on 2022-11-18 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricing',
            old_name='idpricing',
            new_name='pricingid',
        ),
        migrations.RenameField(
            model_name='pricing',
            old_name='productid',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='productdiscount',
            old_name='productid',
            new_name='product',
        ),
    ]