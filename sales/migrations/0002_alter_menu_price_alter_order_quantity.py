# Generated by Django 4.2.1 on 2023-05-15 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
