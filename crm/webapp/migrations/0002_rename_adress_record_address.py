# Generated by Django 4.2.9 on 2024-01-29 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='adress',
            new_name='address',
        ),
    ]
