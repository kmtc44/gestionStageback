# Generated by Django 2.2.2 on 2019-07-11 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20190711_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(default='', max_length=50),
        ),
    ]
