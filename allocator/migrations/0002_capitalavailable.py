# Generated by Django 2.0.1 on 2018-01-23 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allocator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CapitalAvailable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.IntegerField()),
                ('total_cap', models.FloatField()),
                ('open_cap', models.FloatField()),
            ],
        ),
    ]