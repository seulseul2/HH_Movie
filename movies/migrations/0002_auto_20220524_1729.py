# Generated by Django 3.2.7 on 2022-05-24 08:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='department',
        ),
        migrations.RemoveField(
            model_name='director',
            name='department',
        ),
        migrations.AddField(
            model_name='actor',
            name='like_users',
            field=models.ManyToManyField(related_name='like_actors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='director',
            name='like_users',
            field=models.ManyToManyField(related_name='like_directors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movie',
            name='like_users',
            field=models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]
