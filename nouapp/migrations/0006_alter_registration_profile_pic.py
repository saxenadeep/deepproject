# Generated by Django 5.0.4 on 2024-10-04 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nouapp', '0005_registration_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='profile_pic',
            field=models.ImageField(upload_to=''),
        ),
    ]
