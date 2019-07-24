# Generated by Django 2.2.2 on 2019-07-22 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('internship', '0006_enterprise_logo'),
        ('accounts', '0031_merge_20190722_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConventionMesage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('sended_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('convention', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='internship.Convention')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convMessage', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
