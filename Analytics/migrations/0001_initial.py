# Generated by Django 4.1.3 on 2023-04-08 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Visitor",
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
                ("device", models.CharField(max_length=200)),
                ("date_visited", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
