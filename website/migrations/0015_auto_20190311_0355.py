# Generated by Django 2.1.5 on 2019-03-10 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20190311_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedcards',
            name='cvv',
            field=models.TextField(default='aa', null=True),
        ),
        migrations.AlterField(
            model_name='savedcards',
            name='month',
            field=models.TextField(default='aa', null=True),
        ),
        migrations.AlterField(
            model_name='savedcards',
            name='name',
            field=models.TextField(default='aa', null=True),
        ),
        migrations.AlterField(
            model_name='savedcards',
            name='number',
            field=models.TextField(default='aaa', null=True),
        ),
        migrations.AlterField(
            model_name='savedcards',
            name='year',
            field=models.TextField(default='aa', null=True),
        ),
    ]