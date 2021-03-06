# Generated by Django 2.0.1 on 2018-01-10 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('get_data', '0002_auto_20180110_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_type', models.CharField(max_length=5)),
                ('quantity', models.FloatField()),
                ('rate', models.FloatField()),
                ('time_p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='get_data.PeriodData')),
            ],
        ),
    ]
