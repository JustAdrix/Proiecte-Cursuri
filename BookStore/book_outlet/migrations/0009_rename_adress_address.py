# Generated by Django 5.0.1 on 2024-01-17 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0008_adress_author_address'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Adress',
            new_name='Address',
        ),
    ]