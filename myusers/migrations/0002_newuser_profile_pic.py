# Generated by Django 4.1.5 on 2023-02-09 09:45

from django.db import migrations, models
import myusers.models


class Migration(migrations.Migration):

    dependencies = [
        ('myusers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='profile_pic',
            field=models.ImageField(default='posts/avatar.jpg', upload_to=myusers.models.upload_to, verbose_name='Image'),
        ),
    ]
