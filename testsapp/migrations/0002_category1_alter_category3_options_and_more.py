# Generated by Django 4.2.13 on 2024-07-04 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("testsapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category1",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Category1_name",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=264,
                        null=True,
                        verbose_name=" Category3",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": " Category1",
                "verbose_name_plural": " Category1",
            },
        ),
        migrations.AlterModelOptions(
            name="category3",
            options={"verbose_name": " Category3", "verbose_name_plural": " Category3"},
        ),
        migrations.AlterField(
            model_name="test",
            name="test_origin",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="testsapp.category3",
                verbose_name=" ტესტის კატეგორია",
            ),
        ),
        migrations.CreateModel(
            name="Category2",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Category2_name",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=264,
                        null=True,
                        verbose_name=" Category3",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "Category1_name",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="testsapp.category1",
                        verbose_name=" ტესტის კატეგორია1",
                    ),
                ),
            ],
            options={
                "verbose_name": " Category2",
                "verbose_name_plural": " Category2",
            },
        ),
        migrations.AddField(
            model_name="category3",
            name="Category2_name",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="testsapp.category2",
                verbose_name=" ტესტის კატეგორია",
            ),
        ),
    ]
