# Generated by Django 3.2.24 on 2024-10-09 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0018_rename_photo_userprofile_profile_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey_application',
            name='status',
            field=models.CharField(blank=True, default='Verified', max_length=15, null=True),
        ),
    ]