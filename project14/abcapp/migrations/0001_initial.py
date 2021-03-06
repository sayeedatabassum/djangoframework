# Generated by Django 3.0.7 on 2020-07-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abcstudentdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abcid', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('college', models.CharField(max_length=20)),
                ('branch', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('year_of_pass', models.DateField()),
                ('percentage', models.FloatField()),
                ('phone_number', models.CharField(max_length=50)),
                ('mail_id', models.EmailField(max_length=254)),
            ],
        ),
    ]
