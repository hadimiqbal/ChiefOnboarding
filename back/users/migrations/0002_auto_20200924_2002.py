# Generated by Django 3.0.7 on 2020-09-24 20:02

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="preboardinguser",
            name="form",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                default=list,
                verbose_name=models.TextField(default="[]", max_length=100000),
            ),
        ),
        migrations.AlterField(
            model_name="todouser",
            name="form",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                default=list, verbose_name=models.TextField(default="[]")
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="facebook",
            field=models.CharField(blank=True, default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="user",
            name="linkedin",
            field=models.CharField(blank=True, default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="user",
            name="message",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="user",
            name="twitter",
            field=models.CharField(blank=True, default="", max_length=100),
        ),
    ]
