# Generated by Django 4.1 on 2022-08-19 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Name',
            new_name='name',
        ),
    ]
