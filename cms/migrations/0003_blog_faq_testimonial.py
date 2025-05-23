# Generated by Django 4.2.11 on 2024-07-06 10:04

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globalapp', '0013_delete_basebeneficariesmodel'),
        ('cms', '0002_alter_page_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp.common')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
                ('pub_status', models.CharField(choices=[('DRAFT', 'Draft'), ('PUBLISHED', 'Published')], default='DRAFT', max_length=10)),
                ('image', models.ImageField(upload_to='blog_images/')),
            ],
            bases=('globalapp.common',),
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp.common')),
                ('question', models.CharField(max_length=100)),
                ('answer', ckeditor.fields.RichTextField()),
            ],
            bases=('globalapp.common',),
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp.common')),
                ('author', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
                ('rating', models.IntegerField()),
            ],
            bases=('globalapp.common',),
        ),
    ]
