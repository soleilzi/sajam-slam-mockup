# Generated by Django 5.0.6 on 2024-08-27 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_streamerinfo_coach_streamerinfo_rank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='streamerinfo',
            name='coach',
        ),
        migrations.AlterField(
            model_name='streamerinfo',
            name='twitch',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='streamerinfo',
            name='twitter',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='streamerinfo',
            name='youtube',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
