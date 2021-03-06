# Generated by Django 2.0.1 on 2018-01-22 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('get_data', '0009_auto_20180116_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField()),
                ('coin_symbol', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('price_denominator', models.CharField(max_length=200)),
                ('order_type', models.CharField(max_length=400)),
                ('order_status', models.CharField(max_length=600)),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='get_data.PeriodData')),
            ],
        ),
    ]
