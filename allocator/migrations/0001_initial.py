# Generated by Django 2.0.1 on 2018-01-23 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_symbol', models.CharField(max_length=400)),
                ('position', models.CharField(max_length=7)),
            ],
        ),
    ]