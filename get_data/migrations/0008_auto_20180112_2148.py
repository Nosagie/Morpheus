# Generated by Django 2.0.1 on 2018-01-12 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_data', '0007_auto_20180112_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perioddata',
            name='start_timestamp',
            field=models.CharField(max_length=300),
        ),
    ]
