# Generated by Django 2.2 on 2019-04-10 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20190407_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('amount', models.IntegerField(default=0)),
                ('phone', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
                ('perc', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='BillPay',
        ),
    ]
