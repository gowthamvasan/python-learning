# Generated by Django 3.2.8 on 2021-12-31 01:18

from django.db import migrations, models
import django.db.models.deletion
# Generated by Django 3.2.8 on 2021-12-25 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tb_track_app', '0016_auto_20211117_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobilenumber', models.PositiveIntegerField()),
                ('hearus', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tb_track_app.course')),
            ],
            options={
                'db_table': '"Community_Form"',
            },
        ),
    ]
