# Generated by Django 4.1.6 on 2023-02-09 18:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inrite', '0011_alter_news_author_alter_news_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 9, 18, 43, 43, 370169, tzinfo=datetime.timezone.utc), verbose_name='date_publish'),
        ),
    ]
