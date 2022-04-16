# Generated by Django 3.2.6 on 2021-11-15 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tb_track_app', '0011_auto_20211115_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainerpayment',
            name='payment_reason',
            field=models.CharField(choices=[('Salary', 'Salary'), ('Advance', 'Advance'), ('Bonus', 'Bonus'), ('Commision', 'Commision')], default=1, max_length=12),
        ),
    ]
