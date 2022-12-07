# Generated by Django 4.1.3 on 2022-12-07 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideasDB', '0003_activity_useractivity_customuser_activity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='activity',
        ),
        migrations.AddField(
            model_name='activity',
            name='rating',
            field=models.FloatField(default=3),
            preserve_default=False,
        ),
    ]
