# Generated by Django 3.2.9 on 2021-12-22 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commits',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('owner_name', models.CharField(max_length=128)),
                ('repo_name', models.CharField(max_length=128)),
                ('con_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Contributors',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('owner_name', models.CharField(max_length=128)),
                ('repo_name', models.CharField(max_length=128)),
                ('con_name', models.CharField(max_length=128)),
                ('con_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='date01',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('repo_name', models.CharField(max_length=128)),
                ('date_newest', models.DateTimeField()),
                ('date_local', models.DateTimeField(auto_now=True)),
                ('date_lasttime', models.DateTimeField()),
            ],
        ),
    ]
