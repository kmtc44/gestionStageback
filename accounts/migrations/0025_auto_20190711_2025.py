# Generated by Django 2.2.2 on 2019-07-11 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20190711_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='socialStatus',
            field=models.CharField(default='', max_length=50),
        ),
    ]
