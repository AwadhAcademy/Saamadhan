# Generated by Django 3.2.4 on 2021-11-20 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_consultant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consultant',
            old_name='phone',
            new_name='phone_number',
        ),
    ]
