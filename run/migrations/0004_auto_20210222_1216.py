# Generated by Django 2.2.13 on 2021-02-22 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('run', '0003_auto_20210209_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
