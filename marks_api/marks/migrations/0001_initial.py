# Generated by Django 3.0.5 on 2020-04-04 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unnamed', max_length=64)),
                ('latti', models.FloatField()),
                ('longi', models.FloatField()),
                ('author', models.CharField(default='???', max_length=64)),
                ('addrdate', models.CharField(max_length=64)),
                ('photo', models.URLField()),
                ('graffity', models.BooleanField()),
                ('onspot', models.BooleanField()),
            ],
        ),
    ]
