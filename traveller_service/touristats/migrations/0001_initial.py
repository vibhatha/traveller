# Generated by Django 4.2.18 on 2025-01-18 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllCountryStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('passengers', models.IntegerField()),
            ],
        ),
    ]