# Generated by Django 4.1.3 on 2022-11-18 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_order_datecomplete_alter_order_dateplaceorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='dateplaceorder',
            field=models.DateTimeField(default='2022-11-18T14:35:38Z'),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
