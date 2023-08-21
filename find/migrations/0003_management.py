# Generated by Django 2.2 on 2023-08-12 05:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('find', '0002_auto_20230810_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jobname', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('avatar', models.ImageField(blank=True, upload_to='job/%Y%m%d/')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
