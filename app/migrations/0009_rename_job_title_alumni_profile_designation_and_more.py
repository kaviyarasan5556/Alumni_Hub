# Generated by Django 4.2.7 on 2025-04-16 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alumni_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumni_profile',
            old_name='job_title',
            new_name='designation',
        ),
        migrations.RenameField(
            model_name='alumni_profile',
            old_name='passedout',
            new_name='passout_year',
        ),
        migrations.RenameField(
            model_name='alumni_profile',
            old_name='Profile_Picture',
            new_name='profile_picture',
        ),
    ]
