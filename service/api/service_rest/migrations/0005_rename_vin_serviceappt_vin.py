# Generated by Django 4.0.3 on 2022-12-09 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0004_alter_serviceappt_vin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceappt',
            old_name='vin',
            new_name='VIN',
        ),
    ]
