# Generated by Django 3.2.24 on 2024-11-04 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0033_alter_survey_application_survey_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey_application',
            name='Survey_Category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='survey_application',
            name='depth',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='survey_application',
            name='height',
            field=models.PositiveIntegerField(),
        ),
    ]
