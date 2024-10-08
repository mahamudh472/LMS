# Generated by Django 5.0.6 on 2024-07-11 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_bookrequest_book_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookrequest',
            name='accepted',
        ),
        migrations.RemoveField(
            model_name='bookrequest',
            name='returned',
        ),
        migrations.AddField(
            model_name='bookrequest',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('received', 'Received'), ('returned', 'Returned')], max_length=20, null=True),
        ),
    ]
