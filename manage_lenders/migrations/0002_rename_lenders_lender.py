# Generated by Django 3.2.3 on 2021-09-08 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_lenders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lenders',
            new_name='Lender',
        ),
    ]