# Generated by Django 4.2.13 on 2024-07-05 09:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("testsapp", "0007_category2_testimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="userident",
            name="coins",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="userident",
            name="points",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]