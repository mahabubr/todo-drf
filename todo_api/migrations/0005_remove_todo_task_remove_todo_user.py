# Generated by Django 4.2.5 on 2023-09-29 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0004_remove_todo_timestamp_remove_todo_updated_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='task',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
    ]
