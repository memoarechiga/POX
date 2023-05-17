# Generated by Django 4.2.1 on 2023-05-16 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_alter_order_price_alter_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.TimeField(),
        ),
    ]