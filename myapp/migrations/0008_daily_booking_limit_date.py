# Generated by Django 3.2.7 on 2021-09-16 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_daily_booking_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily_booking_limit',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
