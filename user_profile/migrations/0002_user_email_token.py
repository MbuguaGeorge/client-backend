# Generated by Django 4.1 on 2022-08-20 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_token',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]