# Generated by Django 3.2.6 on 2022-03-23 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupons',
            name='coupan_code',
            field=models.IntegerField(default=0),
        ),
    ]