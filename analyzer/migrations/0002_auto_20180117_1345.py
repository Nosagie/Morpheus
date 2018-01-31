# Generated by Django 2.0.1 on 2018-01-17 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoPairs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pair', models.CharField(max_length=70)),
            ],
        ),
        migrations.AddField(
            model_name='periodsignals',
            name='period',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='periodsignals',
            name='pair',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analyzer.CryptoPairs'),
        ),
    ]