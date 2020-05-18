# Generated by Django 3.0.5 on 2020-05-18 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Champion', max_length=254)),
                ('championId', models.CharField(default='hm', max_length=254)),
                ('cost', models.IntegerField(default=0)),
                ('trait1', models.CharField(default='Blank1', max_length=254)),
                ('trait2', models.CharField(default='Blank2', max_length=254)),
                ('trait3', models.CharField(default='Blank3', max_length=254)),
            ],
        ),
    ]
