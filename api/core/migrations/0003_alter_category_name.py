# Generated by Django 4.1.3 on 2022-11-18 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_idproduct_product_productid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=45, unique=True),
        ),
    ]
