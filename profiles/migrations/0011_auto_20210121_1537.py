# Generated by Django 3.1.4 on 2021-01-21 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20210121_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='default-profile-picture.jpg', upload_to='profile_img'),
        ),
    ]
