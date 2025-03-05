# Generated by Django 5.0.6 on 2025-02-24 09:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dashboard",
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
                    "first_class",
                    models.CharField(
                        choices=[
                            ("A", "A"),
                            ("A+", "A+"),
                            ("B", "B"),
                            ("B+", "B+"),
                            ("C", "C"),
                            ("C+", "C+"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "second_class",
                    models.CharField(
                        choices=[
                            ("A", "A"),
                            ("A+", "A+"),
                            ("B", "B"),
                            ("B+", "B+"),
                            ("C", "C"),
                            ("C+", "C+"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "third_class",
                    models.CharField(
                        choices=[
                            ("A", "A"),
                            ("A+", "A+"),
                            ("B", "B"),
                            ("B+", "B+"),
                            ("C", "C"),
                            ("C+", "C+"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "fourth_class",
                    models.CharField(
                        choices=[
                            ("A", "A"),
                            ("A+", "A+"),
                            ("B", "B"),
                            ("B+", "B+"),
                            ("C", "C"),
                            ("C+", "C+"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "fifth_class",
                    models.CharField(
                        choices=[
                            ("A", "A"),
                            ("A+", "A+"),
                            ("B", "B"),
                            ("B+", "B+"),
                            ("C", "C"),
                            ("C+", "C+"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
    ]
