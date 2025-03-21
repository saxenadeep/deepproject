# Generated by Django 5.0.4 on 2024-10-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nouapp', '0006_alter_registration_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='usm',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('program', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=100)),
                ('new_file', models.FileField(upload_to='myimage')),
            ],
        ),
    ]
