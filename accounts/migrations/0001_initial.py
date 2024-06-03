# Generated by Django 5.0.6 on 2024-05-29 16:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift', models.CharField(blank=True, max_length=20, null=True)),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('name_bangla', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('father_name', models.CharField(blank=True, max_length=50, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('post_office', models.CharField(blank=True, max_length=50, null=True)),
                ('upazila', models.CharField(blank=True, max_length=50, null=True)),
                ('district', models.CharField(blank=True, max_length=50, null=True)),
                ('number', models.CharField(blank=True, max_length=50, null=True)),
                ('parent_number', models.CharField(blank=True, max_length=50, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=50, null=True)),
                ('technology_code', models.CharField(blank=True, max_length=50, null=True)),
                ('semester', models.CharField(blank=True, max_length=50, null=True)),
                ('birth_date', models.CharField(blank=True, max_length=50, null=True)),
                ('ssc_roll', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='student')),
                ('parent_signature', models.ImageField(blank=True, null=True, upload_to='signature')),
                ('policy_agreement', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]