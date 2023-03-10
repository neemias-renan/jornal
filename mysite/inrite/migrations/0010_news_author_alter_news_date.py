# Generated by Django 4.1.6 on 2023-02-09 17:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inrite', '0009_alter_news_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inrite.profile'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 9, 17, 14, 0, 894765, tzinfo=datetime.timezone.utc), verbose_name='date_publish'),
        ),
    ]
