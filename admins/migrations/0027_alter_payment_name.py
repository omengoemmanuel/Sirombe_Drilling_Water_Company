# Generated by Django 3.2.24 on 2024-10-18 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0026_alter_payment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='name',
            field=models.CharField(choices=[('Symmetric Drilling', 'Symmetric Drilling'), ('Core Drilling', 'Core Drilling'), ('Geo-Technical Drilling', 'Geo-Technical Drilling')], max_length=50),
        ),
    ]