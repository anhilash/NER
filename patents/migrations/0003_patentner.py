# Generated by Django 3.0.5 on 2020-11-07 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patents', '0002_fileuploadhistory_executed'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatentNer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('year', models.IntegerField()),
                ('default_entities', models.TextField()),
                ('custom_entities', models.TextField()),
            ],
        ),
    ]
