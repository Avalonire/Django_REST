# Generated by Django 4.1.2 on 2023-01-23 15:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_book_biography_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('repo_link', models.URLField(max_length=128)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.author')),
            ],
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_text', models.TextField()),
                ('create_date', models.DateTimeField(verbose_name=datetime.datetime)),
                ('update_date', models.DateTimeField(verbose_name=datetime.datetime(2023, 1, 23, 19, 1, 5, 66757))),
                ('condition', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.author')),
                ('for_project', models.ManyToManyField(to='todo.project')),
            ],
        ),
    ]
