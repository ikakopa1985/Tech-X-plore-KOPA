# Generated by Django 4.2.13 on 2024-05-29 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TestOrigin",
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
                    "name",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=264,
                        null=True,
                        verbose_name=" ტესტის წარმომავლობა",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": " Test Origion",
                "verbose_name_plural": " Test Origion",
            },
        ),
        migrations.CreateModel(
            name="TestType",
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
                    "test_type_name",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=264,
                        null=True,
                        verbose_name=" ტესტის ტიპი",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": " Test Type",
                "verbose_name_plural": " Test Type",
            },
        ),
        migrations.CreateModel(
            name="UserIdent",
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
                    "full_name",
                    models.CharField(max_length=50, verbose_name="full name"),
                ),
                (
                    "personal_number",
                    models.CharField(max_length=50, verbose_name="peronal number"),
                ),
                ("birth_date", models.DateField(verbose_name="birth date")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Test",
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
                    "number",
                    models.IntegerField(
                        blank=True, default=None, null=True, verbose_name=" ნომერი"
                    ),
                ),
                (
                    "testText",
                    models.TextField(
                        blank=True,
                        default=None,
                        null=True,
                        verbose_name=" ტესტის შინაარსი",
                    ),
                ),
                (
                    "testDescription",
                    models.TextField(
                        blank=True,
                        default=None,
                        max_length=5264,
                        null=True,
                        verbose_name=" აღწერა",
                    ),
                ),
                (
                    "testImage",
                    models.ImageField(
                        blank=True,
                        default=None,
                        null=True,
                        upload_to="photos/proposition/%y/%m/%d/",
                        verbose_name=" ფოტო",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "test_origin",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="testsapp.testorigin",
                        verbose_name=" ტესტის წარმომავლობა",
                    ),
                ),
                (
                    "test_type",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="testsapp.testtype",
                        verbose_name=" ტესტის ტიპი",
                    ),
                ),
            ],
            options={
                "verbose_name": " Tests",
                "verbose_name_plural": " Tests",
            },
        ),
        migrations.CreateModel(
            name="Answers",
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
                    "answer_text",
                    models.TextField(
                        blank=True,
                        default=None,
                        null=True,
                        verbose_name=" პასუხის შინაარსი",
                    ),
                ),
                ("is_correct", models.BooleanField(default=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "tests",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="testsapp.test",
                        verbose_name=" ტესტის ტიპი",
                    ),
                ),
            ],
            options={
                "verbose_name": " answers",
                "verbose_name_plural": " answers",
            },
        ),
    ]
