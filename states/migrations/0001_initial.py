# Generated by Django 2.1.7 on 2019-03-20 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('capital', models.CharField(max_length=200)),
                ('created_on', models.PositiveIntegerField()),
                ('created_from', models.CharField(blank=True, default='N/A', max_length=200, null=True)),
                ('governor', models.CharField(max_length=500)),
                ('deputy_governor', models.CharField(blank=True, default='N/A', max_length=500, null=True)),
                ('geopolitical_zone', models.CharField(choices=[('north_central', 'north central'), ('north_east', 'north east'), ('north_west', 'north west'), ('south_east', 'south east'), ('south_south', 'south south'), ('south_west', 'south west')], max_length=100)),
                ('slogan', models.CharField(max_length=400)),
                ('no_of_local_governments', models.PositiveIntegerField(default='N/A')),
                ('denonyms', models.CharField(blank=True, default='N/A', max_length=400, null=True)),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
