# Generated by Django 4.2.7 on 2025-04-13 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_studentsignup_roll_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnisignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=30)),
                ('passedout', models.IntegerField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=30)),
            ],
        ),
    ]
