# Generated by Django 3.2.6 on 2021-11-12 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tb_track_app', '0006_rename_traineerfees_trainerfees'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainerfees',
            name='total_salary_paid',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
