# Generated by Django 3.2.7 on 2021-10-04 05:39

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20211003_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='mobile',
            field=models.CharField(max_length=10, null=True, validators=[myapp.models.mobile]),
        ),
        migrations.AlterField(
            model_name='doctorprofile',
            name='mobile',
            field=models.CharField(max_length=10, null=True, validators=[myapp.models.mobile]),
        ),
    ]
