# Generated by Django 5.1.6 on 2025-03-03 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='heartrate',
            old_name='user_id',
            new_name='user',
        ),
    ]
