# Generated by Django 2.1.2 on 2019-07-16 16:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='like_post', to=settings.AUTH_USER_MODEL),
        ),
    ]