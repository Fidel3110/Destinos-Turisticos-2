# Generated by Django 3.0.7 on 2020-07-10 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_auto_20200709_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
    ]
