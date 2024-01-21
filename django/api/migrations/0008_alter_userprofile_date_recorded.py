# Generated by Django 4.2.7 on 2024-01-16 17:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_userprofile_date_recorded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_recorded',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]