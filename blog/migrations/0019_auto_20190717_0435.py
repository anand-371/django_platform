# Generated by Django 2.1.2 on 2019-07-16 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_post_domain'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='Subject',
        ),
    ]