# Generated by Django 5.0.4 on 2024-10-07 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nouapp', '0008_rename_usm_tbl_usm'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload_lecture',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('program', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
