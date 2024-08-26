# Generated by Django 3.2.8 on 2021-10-22 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_alter_labbooking_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('vaccancies', models.IntegerField(default=1)),
                ('description', models.TextField()),
            ],
        ),
    ]
