# Generated by Django 4.2.4 on 2023-08-18 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0003_song_is_published_song_scheduled_publish_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
