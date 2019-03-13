# Generated by Django 2.1.7 on 2019-03-09 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airports', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airport',
            name='town',
        ),
        migrations.AlterField(
            model_name='airport',
            name='type',
            field=models.CharField(choices=[('domestic', 'domestic'), ('international', 'international')], max_length=100),
        ),
        migrations.AlterField(
            model_name='airport',
            name='website',
            field=models.URLField(blank=True, default='N/A', null=True),
        ),
    ]
