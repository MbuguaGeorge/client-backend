# Generated by Django 4.0 on 2022-10-22 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_academic_writing_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='academic_writing',
            name='spacing',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]