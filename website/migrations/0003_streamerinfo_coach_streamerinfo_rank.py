# Generated by Django 5.0.6 on 2024-08-21 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_streamerinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='streamerinfo',
            name='coach',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='streamerinfo',
            name='rank',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
