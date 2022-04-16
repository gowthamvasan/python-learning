# Generated by Django 3.2.8 on 2021-12-31 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tb_track_app', '0017_communityform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communityform',
            name='course',
        ),
        migrations.RemoveField(
            model_name='communityform',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='communityform',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='communityform',
            name='mobilenumber',
        ),
        migrations.AddField(
            model_name='communityform',
            name='first_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='communityform',
            name='last_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='communityform',
            name='phone',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='communityform',
            name='technology',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='communityform',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='communityform',
            name='hearus',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
