# Generated by Django 4.1.3 on 2022-11-18 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_idpricing_pricing_pricingid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='in_active',
            field=models.BooleanField(),
        ),
    ]
