# Generated by Django 3.1.1 on 2020-09-27 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20200926_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='default.png', upload_to='author-avatars/%Y')),
                ('bio', models.TextField(blank=True, null=True)),
                ('website', models.URLField(blank=True, help_text='Enter URL to anywhere on the web we can find your content.', null=True)),
                ('twitter', models.URLField(blank=True, help_text='Enter URL to your twitter profile.', null=True)),
                ('facebook', models.URLField(blank=True, help_text='Enter URL to your facebook profile.', null=True)),
                ('instagram', models.URLField(blank=True, help_text='Enter URL to your instagram profile.', null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
