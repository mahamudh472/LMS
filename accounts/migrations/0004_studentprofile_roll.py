# Generated by Django 5.0.6 on 2024-07-05 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_studentprofile_is_active_alter_studentprofile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='roll',
            field=models.CharField(blank=True, default='000000', max_length=50, null=True),
        ),
    ]
