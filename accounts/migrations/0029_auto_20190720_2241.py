# Generated by Django 2.2.2 on 2019-07-20 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_attachments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachments',
            name='cv',
            field=models.FileField(null=True, upload_to='cv/'),
        ),
    ]