# Generated by Django 3.2.6 on 2021-11-12 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tb_track_app', '0007_trainerfees_total_salary_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainerfees',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tb_track_app.trainer'),
        ),
    ]
