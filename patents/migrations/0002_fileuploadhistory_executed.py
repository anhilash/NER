# Generated by Django 3.0.5 on 2020-11-06 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileuploadhistory',
            name='executed',
            field=models.BooleanField(default=False),
        ),
    ]
