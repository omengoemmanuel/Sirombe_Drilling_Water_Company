# Generated by Django 3.2.24 on 2024-11-11 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0008_alter_booking_query_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='pick_time',
            field=models.TimeField(),
        ),
    ]