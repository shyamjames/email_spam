# Generated by Django 3.2.23 on 2024-02-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='datetime',
            new_name='date_time',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='datetime',
            new_name='date_time',
        ),
        migrations.AddField(
            model_name='complaint',
            name='date_time',
            field=models.CharField(default='pending', max_length=255),
        ),
        migrations.AddField(
            model_name='complaint',
            name='subject',
            field=models.CharField(default='pending', max_length=255),
        ),
    ]
