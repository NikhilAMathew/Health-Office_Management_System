# Generated by Django 3.2.7 on 2021-09-16 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_labbooking_symptoms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily_booking_limit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit', models.IntegerField()),
            ],
        ),
    ]
