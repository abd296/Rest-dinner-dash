# Generated by Django 4.0.6 on 2022-08-01 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maindisplay', '0002_item_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='order_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Item Order Count'),
        ),
    ]