# Generated by Django 4.1.3 on 2022-12-11 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideasDB', '0006_rename_user_id_activity_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='completed_on',
        ),
        migrations.AddField(
            model_name='activity',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
