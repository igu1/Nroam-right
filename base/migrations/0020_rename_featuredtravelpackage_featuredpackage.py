# Generated by Django 4.1.7 on 2023-03-14 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_rename_agency_agencie_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FeaturedTravelPackage',
            new_name='FeaturedPackage',
        ),
    ]
