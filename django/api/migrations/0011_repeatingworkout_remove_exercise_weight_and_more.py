# Generated by Django 4.2.7 on 2024-01-16 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepeatingWorkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_date', models.DateField()),
                ('ending_date', models.DateField()),
                ('frequency', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='weight',
        ),
        migrations.AddField(
            model_name='exercise',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='exercise',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='repeatingWorkout',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.repeatingworkout'),
        ),
    ]