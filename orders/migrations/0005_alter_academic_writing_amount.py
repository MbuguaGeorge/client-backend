# Generated by Django 4.0 on 2022-09-01 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_academic_writing_amount_academic_writing_discipline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic_writing',
            name='amount',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
