# Generated by Django 2.1.5 on 2019-03-10 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_savedcards_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedcards',
            name='password',
            field=models.CharField(default='111111111111111', max_length=15, null=True),
        ),
    ]
