# Generated by Django 2.0.5 on 2018-05-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picksong', '0003_auto_20180522_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='song',
        ),
        migrations.AddField(
            model_name='song',
            name='name',
            field=models.TextField(default='none'),
        ),
        migrations.AlterField(
            model_name='song',
            name='highest_note',
            field=models.TextField(default='none'),
        ),
        migrations.AlterField(
            model_name='song',
            name='key_of_song',
            field=models.TextField(default='none'),
        ),
        migrations.AlterField(
            model_name='song',
            name='lowest_note',
            field=models.TextField(default='none'),
        ),
        migrations.AlterField(
            model_name='song',
            name='owner',
            field=models.TextField(default='none'),
        ),
    ]
