# Generated by Django 4.2.11 on 2024-05-04 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globalapp', '0004_alter_basebeneficariesmodel_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basebeneficariesmodel',
            name='profile_picture',
            field=models.ImageField(default='profile_pictures/profile-picture.jpg', upload_to='profile_pictures/'),
        ),
    ]
