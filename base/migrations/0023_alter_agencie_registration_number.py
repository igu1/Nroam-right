# Generated by Django 4.1.7 on 2023-03-14 16:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_alter_agencie_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencie',
            name='registration_number',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]