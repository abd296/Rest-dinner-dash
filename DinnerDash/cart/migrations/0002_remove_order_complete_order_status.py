# Generated by Django 4.0.6 on 2022-08-01 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='complete',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('cart', 'cart'), ('ordered', 'ordered'), ('paid', 'paid'), ('cancelled', 'cancelled'), ('completed', 'completed')], default='cart', max_length=20, verbose_name='order status'),
        ),
    ]
