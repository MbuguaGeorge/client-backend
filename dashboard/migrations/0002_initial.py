# Generated by Django 4.0 on 2022-11-04 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recent_orders',
            name='details',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.academic_writing'),
        ),
    ]
