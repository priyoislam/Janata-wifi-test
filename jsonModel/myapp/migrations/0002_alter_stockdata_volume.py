# Generated by Django 4.2.7 on 2023-12-09 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdata',
            name='volume',
            field=models.CharField(max_length=20),
        ),
    ]
