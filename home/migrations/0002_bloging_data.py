# Generated by Django 3.2.4 on 2021-11-15 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bloging_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('information', models.CharField(max_length=5000)),
                ('image', models.ImageField(default='', upload_to='base/images')),
                ('hyper_link', models.CharField(max_length=100)),
            ],
        ),
    ]
