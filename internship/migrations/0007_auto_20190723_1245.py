# Generated by Django 2.2.2 on 2019-07-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0006_enterprise_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprise',
            name='latitude',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='enterprise',
            name='longitude',
            field=models.IntegerField(null=True),
        ),
    ]
