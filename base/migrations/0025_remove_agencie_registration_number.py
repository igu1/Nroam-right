# Generated by Django 4.1.7 on 2023-03-14 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_alter_agencie_registration_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agencie',
            name='registration_number',
        ),
    ]
