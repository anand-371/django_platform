# Generated by Django 2.1.2 on 2019-07-14 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
