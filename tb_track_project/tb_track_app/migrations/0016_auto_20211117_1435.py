# Generated by Django 3.2.6 on 2021-11-17 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tb_track_app', '0015_auto_20211116_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traineeenroll',
            name='notify_future_batch',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='traineeenroll',
            name='up_batch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tb_track_app.upcomingbatch'),
        ),
    ]