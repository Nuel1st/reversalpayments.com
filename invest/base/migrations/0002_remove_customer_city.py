# Generated by Django 4.1.4 on 2024-03-02 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='city',
        ),
    ]
