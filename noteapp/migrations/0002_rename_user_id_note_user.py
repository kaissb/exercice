# Generated by Django 4.1.2 on 2022-10-19 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='user_id',
            new_name='user',
        ),
    ]
