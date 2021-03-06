# Generated by Django 3.2.8 on 2021-12-31 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tb_track_app', '0020_auto_20211231_0854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='communityform',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='communityform',
            old_name='last_name',
            new_name='lastname',
        ),
        migrations.AlterField(
            model_name='communityform',
            name='technology',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tb_track_app.course'),
        ),
    ]
