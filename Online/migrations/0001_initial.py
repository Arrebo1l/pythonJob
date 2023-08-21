# Generated by Django 2.2 on 2023-08-03 06:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineDoctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
