# Generated by Django 4.2.11 on 2025-05-11 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeritListEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=100)),
                ('batch', models.CharField(max_length=10)),
                ('roll', models.CharField(max_length=20, unique=True)),
                ('marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rank', models.PositiveIntegerField()),
                ('sl', models.PositiveIntegerField(verbose_name='Serial')),
                ('subject', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=50)),
            ],
        ),
    ]
