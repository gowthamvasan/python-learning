# Generated by Django 3.2.6 on 2021-11-15 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tb_track_app', '0012_trainerpayment_payment_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainerpayment',
            name='amount_to_be_paid',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
