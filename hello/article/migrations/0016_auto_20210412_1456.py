# Generated by Django 3.1.6 on 2021-04-12 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_auto_20210412_1444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'permissions': [('сan_have_piece_of_pizza', 'Может съесть кусочек пиццы')], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
