# Generated by Django 4.1.3 on 2022-12-12 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideasDB', '0008_cuisine_activity_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='review',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
