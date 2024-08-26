# Generated by Django 3.2.7 on 2021-10-07 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20211003_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='district',
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='land_mark',
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='road',
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='state',
        ),
        migrations.RemoveField(
            model_name='doctorprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='doctorprofile',
            name='district',
        ),
        migrations.RemoveField(
            model_name='doctorprofile',
            name='land_mark',
        ),
        migrations.RemoveField(
            model_name='doctorprofile',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='doctorprofile',
            name='road',
        ),
        migrations.RemoveField(
            model_name='hi',
            name='city',
        ),
        migrations.RemoveField(
            model_name='hi',
            name='district',
        ),
        migrations.RemoveField(
            model_name='hi',
            name='land_mark',
        ),
        migrations.RemoveField(
            model_name='hi',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='hi',
            name='road',
        ),
        migrations.RemoveField(
            model_name='hi',
            name='state',
        ),
        migrations.RemoveField(
            model_name='lab',
            name='city',
        ),
        migrations.RemoveField(
            model_name='lab',
            name='district',
        ),
        migrations.RemoveField(
            model_name='lab',
            name='land_mark',
        ),
        migrations.RemoveField(
            model_name='lab',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='lab',
            name='road',
        ),
        migrations.RemoveField(
            model_name='lab',
            name='state',
        ),
        migrations.RemoveField(
            model_name='vacancyapply',
            name='city',
        ),
        migrations.RemoveField(
            model_name='vacancyapply',
            name='district',
        ),
        migrations.RemoveField(
            model_name='vacancyapply',
            name='land_mark',
        ),
        migrations.RemoveField(
            model_name='vacancyapply',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='vacancyapply',
            name='road',
        ),
        migrations.RemoveField(
            model_name='vacancyapply',
            name='state',
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='address',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='address',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='hi',
            name='address',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='lab',
            name='address',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='vacancyapply',
            name='address',
            field=models.TextField(default=True),
        ),
    ]
