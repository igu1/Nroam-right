# Generated by Django 4.1.7 on 2023-03-14 02:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_rename_start_data_travelpackage_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelpackage',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]