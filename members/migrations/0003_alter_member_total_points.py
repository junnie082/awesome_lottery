# Generated by Django 5.0.6 on 2025-02-21 07:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0002_alter_member_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="total_points",
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
