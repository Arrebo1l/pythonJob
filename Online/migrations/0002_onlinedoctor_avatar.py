# Generated by Django 2.2 on 2023-08-06 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Online', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinedoctor',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='doctor/%Y%m%d/'),
        ),
    ]
