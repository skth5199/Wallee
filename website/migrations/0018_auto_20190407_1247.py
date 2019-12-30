# Generated by Django 2.1.4 on 2019-04-07 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0017_auto_20190404_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillPay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
                ('cost', models.IntegerField(default=100)),
                ('starting', models.TextField(default=False)),
                ('dest', models.TextField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
                ('pcat', models.TextField(default='Electricity')),
            ],
        ),
        migrations.CreateModel(
            name='TicketBookBus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('seats', models.IntegerField(default=1)),
                ('amount', models.IntegerField(default=0)),
                ('bus', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='website.Bus')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ticketbook',
            name='seats',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='billpay',
            name='provider',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='website.Provider'),
        ),
        migrations.AddField(
            model_name='billpay',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]