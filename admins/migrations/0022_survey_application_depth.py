# Generated by Django 3.2.24 on 2024-10-18 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0021_auto_20241012_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey_application',
            name='depth',
            field=models.PositiveIntegerField(default='0', null=True),
        ),
    ]
