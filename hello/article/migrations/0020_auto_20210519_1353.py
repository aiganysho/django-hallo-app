# Generated by Django 3.1.6 on 2021-05-19 13:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0019_article_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='like_comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='like_article', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
