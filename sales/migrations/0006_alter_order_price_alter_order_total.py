# Generated by Django 4.2.1 on 2023-05-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_alter_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]