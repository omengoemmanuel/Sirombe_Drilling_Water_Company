# Generated by Django 3.2.24 on 2024-10-09 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0019_survey_application_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey_application',
            name='status',
            field=models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Verified', 'Verified')], default='Verified', max_length=15, null=True),
        ),
    ]