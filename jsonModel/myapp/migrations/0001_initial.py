# Generated by Django 4.2.7 on 2023-12-09 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('trade_code', models.CharField(max_length=20)),
                ('high', models.DecimalField(decimal_places=2, max_digits=5)),
                ('low', models.DecimalField(decimal_places=2, max_digits=5)),
                ('open', models.DecimalField(decimal_places=2, max_digits=5)),
                ('close', models.DecimalField(decimal_places=2, max_digits=5)),
                ('volume', models.BigIntegerField()),
            ],
        ),
    ]
