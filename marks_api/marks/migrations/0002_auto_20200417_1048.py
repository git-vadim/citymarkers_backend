# Generated by Django 3.0.5 on 2020-04-17 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='graffity',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='onspot',
        ),
        migrations.AddField(
            model_name='mark',
            name='status',
            field=models.CharField(default='onspot', max_length=10),
        ),
        migrations.AddField(
            model_name='mark',
            name='typeof',
            field=models.CharField(default='graffity', max_length=10),
        ),
    ]