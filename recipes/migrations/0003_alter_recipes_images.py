# Generated by Django 3.2 on 2021-04-30 13:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipes_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='images',
            field=models.ImageField(default=datetime.datetime(2021, 4, 30, 13, 4, 1, 794107, tzinfo=utc), upload_to='media/'),
        ),
    ]
