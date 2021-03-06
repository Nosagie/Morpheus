# Generated by Django 2.0.1 on 2018-01-17 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodSignals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_score', models.IntegerField(default=None, null=True)),
                ('cumulative_score', models.IntegerField(default=None, null=True)),
                ('backShort', models.FloatField(default=None, null=True)),
                ('backLong', models.FloatField(default=None, null=True)),
                ('action', models.CharField(max_length=300)),
                ('pair', models.CharField(max_length=300)),
                ('rate', models.FloatField()),
            ],
        ),
    ]
