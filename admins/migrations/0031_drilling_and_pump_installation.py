# Generated by Django 3.2.24 on 2024-10-24 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0030_tank'),
    ]

    operations = [
        migrations.CreateModel(
            name='drilling_and_pump_installation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceType', models.CharField(max_length=50)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=14)),
                ('status', models.CharField(max_length=20)),
                ('depth', models.PositiveIntegerField()),
                ('down_payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('drilling_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pumpType', models.CharField(max_length=50)),
                ('pump_payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('height', models.PositiveIntegerField()),
                ('pipe_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tankType', models.CharField(max_length=50)),
                ('tank_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pump_tank_fee', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
