# Generated by Django 4.0.6 on 2022-07-30 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maindisplay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Item Available'),
        ),
    ]
