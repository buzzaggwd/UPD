# Generated by Django 5.2.1 on 2025-05-24 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upd', '0006_alter_shipping_address_alter_shipping_inn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='relation_type',
            field=models.CharField(),
        ),
    ]
