# Generated by Django 4.1.7 on 2023-03-14 17:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_alter_agencie_registration_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencie',
            name='registration_number',
            field=models.UUIDField(blank=True, default=uuid.uuid4, null=True, unique=True),
        ),
    ]
