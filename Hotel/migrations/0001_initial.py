# Generated by Django 3.2.9 on 2021-12-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cusid', models.IntegerField()),
                ('cusname', models.TextField(max_length=30)),
                ('cusmail', models.EmailField(max_length=30)),
                ('cuspass', models.TextField(max_length=30)),
            ],
        ),
    ]
