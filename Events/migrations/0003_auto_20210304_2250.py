# Generated by Django 3.1.6 on 2021-03-04 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0002_auto_20210303_2340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='atendees',
            new_name='attendees',
        ),
    ]