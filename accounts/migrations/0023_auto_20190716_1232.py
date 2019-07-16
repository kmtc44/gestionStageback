# Generated by Django 2.2.2 on 2019-07-16 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_merge_20190710_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[('Created', 'Created'), ('Doing', 'Doing'), ('Done', 'Done'), ('Reviewing', 'Reviewing'), ('Finish', 'Finish')], default='Created', max_length=30),
        ),
        migrations.AlterField(
            model_name='project',
            name='framer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_project', to='accounts.Framer'),
        ),
    ]
