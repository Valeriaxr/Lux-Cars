# Generated by Django 4.0.3 on 2022-12-09 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0007_automobilevo_color_automobilevo_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automobilevo',
            name='year',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
