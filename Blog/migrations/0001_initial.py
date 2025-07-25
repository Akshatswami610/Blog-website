# Generated by Django 5.2.3 on 2025-07-10 04:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('subject', models.CharField(default='', max_length=50)),
                ('message', models.CharField(default=500)),
            ],
        ),
        migrations.CreateModel(
            name='Blog_post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(max_length=50)),
                ('author', models.CharField(default='', max_length=50)),
                ('content', models.CharField(default='', max_length=50)),
                ('image', models.ImageField(default='', upload_to='blog/images')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
