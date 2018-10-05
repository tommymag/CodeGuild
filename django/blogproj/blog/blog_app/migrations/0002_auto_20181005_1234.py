# Generated by Django 2.0 on 2018-10-05 19:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('date_created', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_text',
            field=models.TextField(default='I am writing in my blog'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='bio_text',
            field=models.TextField(max_length=511),
        ),
        migrations.AddField(
            model_name='post',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_app.Blog'),
        ),
    ]
