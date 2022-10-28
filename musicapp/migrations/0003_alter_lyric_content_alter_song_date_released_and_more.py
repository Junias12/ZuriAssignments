# Generated by Django 4.1.2 on 2022-10-28 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_lyric_artiste_song_artiste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyric',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='date_released',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]