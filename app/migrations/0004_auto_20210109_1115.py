# Generated by Django 2.2.17 on 2021-01-09 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_work'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Work',
            new_name='Blog',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
