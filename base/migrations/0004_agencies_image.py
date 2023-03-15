# Generated by Django 4.1.7 on 2023-03-13 17:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_review_for_agency'),
    ]

    operations = [
        migrations.AddField(
            model_name='agencies',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='', verbose_name='/uploads/agencies'),
            preserve_default=False,
        ),
    ]