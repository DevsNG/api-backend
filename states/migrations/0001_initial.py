# Generated by Django 2.1.7 on 2019-03-09 23:29

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
                ('created_from', models.PositiveIntegerField(blank=True, default='N/A', null=True)),
                ('governor', models.CharField(max_length=500)),
                ('vice_governor', models.CharField(blank=True, default='N/A', max_length=500, null=True)),
                ('geopolitical_zone', models.CharField(max_length=100)),
                ('slogan', models.CharField(max_length=400)),
                ('no_of_local_governments', models.SmallIntegerField(default='N/A')),
                ('denonyms', models.CharField(blank=True, default='N/A', max_length=400, null=True)),
                ('landmarks', models.CharField(max_length=1000)),
                ('website', models.URLField(blank=True, default='N/A', null=True)),
            ],
        ),
    ]
