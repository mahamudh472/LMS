# Generated by Django 5.0.6 on 2024-07-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_bookrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookrequest',
            name='book_time',
            field=models.IntegerField(default=0),
        ),
    ]
