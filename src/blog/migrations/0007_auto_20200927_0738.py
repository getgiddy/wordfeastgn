# Generated by Django 3.1.1 on 2020-09-27 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_authorprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorprofile',
            name='avatar',
            field=models.ImageField(default='default.jpeg', upload_to='author-avatars/%Y'),
        ),
    ]