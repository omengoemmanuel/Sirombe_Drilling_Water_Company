# Generated by Django 3.2.24 on 2024-11-04 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0032_mpesapayment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey_application',
            name='Survey_Category',
            field=models.CharField(default='N/A', max_length=50),
        ),
    ]
