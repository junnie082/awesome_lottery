# Generated by Django 5.0.6 on 2025-02-27 11:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lottery", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="point",
            name="points",
            field=models.IntegerField(default=0),
        ),
    ]
