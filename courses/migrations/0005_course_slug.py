# Generated by Django 4.0.5 on 2022-07-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_video_video_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.CharField(max_length=100, null=True),
        ),
    ]