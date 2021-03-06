# Generated by Django 2.1.5 on 2019-03-10 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0008_auto_20190311_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='bankaccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(default='', null=True)),
                ('number', models.TextField(default='', null=True)),
                ('ifsc', models.TextField(default='', null=True)),
                ('password', models.TextField(default='', null=True)),
                ('amount', models.IntegerField(default=10000)),
            ],
        ),
        migrations.CreateModel(
            name='savedcards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='', null=True)),
                ('number', models.TextField(default='', null=True)),
                ('month', models.TextField(default='', null=True)),
                ('year', models.TextField(default='', null=True)),
                ('cvv', models.TextField(default='')),
                ('amount', models.IntegerField(default=10000)),
                ('ownername', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
