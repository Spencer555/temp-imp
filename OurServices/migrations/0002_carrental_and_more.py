# Generated by Django 4.1.3 on 2023-04-04 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("OurServices", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CarRental",
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
                ("car", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("rate", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "per",
                    models.CharField(
                        choices=[
                            ("Per Hour", "Per Hour"),
                            ("Per Day", "Per Day"),
                            ("Per Week", "Per Week"),
                            ("Per Month", "Per Month"),
                        ],
                        max_length=100,
                    ),
                ),
                ("location", models.CharField(max_length=100)),
                ("contact_no", models.CharField(max_length=30)),
                ("color", models.CharField(max_length=100)),
                ("interior_color", models.CharField(max_length=100)),
                ("accessories", models.TextField()),
                ("main_image", models.ImageField(upload_to=None)),
                (
                    "region",
                    models.CharField(
                        choices=[
                            ("VOLTA ", "VOLTA "),
                            ("BRONG AHAFO ", "BRONG AHAFO "),
                            ("OTI ", "OTI "),
                            ("CENTRAL ", "CENTRAL "),
                            ("EASTERN ", "EASTERN "),
                            ("GREATER ACCRA ", "GREATER ACCRA "),
                            ("NORTH EAST ", "NORTH EAST "),
                            ("NORTHERN ", "NORTHERN "),
                            ("SAVANNAH ", "SAVANNAH "),
                            ("UPPER EAST ", "UPPER EAST "),
                            ("UPPER WEST ", "UPPER WEST "),
                            ("WESTERN ", "WESTERN "),
                            ("WESTERN NORTH ", "WESTERN NORTH "),
                            ("BONO EAST  ", "BONO EAST  "),
                            ("AHAFO ", "AHAFO "),
                            ("ASHANTI ", "ASHANTI "),
                        ],
                        max_length=100,
                    ),
                ),
                ("slug", models.SlugField(blank=True, editable=False, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.RenameField(
            model_name="shipcarforussell",
            old_name="Accessories",
            new_name="accessories",
        ),
        migrations.RemoveField(
            model_name="letussellyourcar",
            name="doors_num",
        ),
        migrations.RemoveField(
            model_name="letussellyourcar",
            name="engine_capacity",
        ),
        migrations.RemoveField(
            model_name="letussellyourcar",
            name="engine_cylinders",
        ),
        migrations.RemoveField(
            model_name="letussellyourcar",
            name="image_5",
        ),
        migrations.RemoveField(
            model_name="letussellyourcar",
            name="seats_num",
        ),
        migrations.RemoveField(
            model_name="shipcarforussell",
            name="doors_num",
        ),
        migrations.RemoveField(
            model_name="shipcarforussell",
            name="engine_capacity",
        ),
        migrations.RemoveField(
            model_name="shipcarforussell",
            name="engine_cylinders",
        ),
        migrations.RemoveField(
            model_name="shipcarforussell",
            name="image_5",
        ),
        migrations.RemoveField(
            model_name="shipcarforussell",
            name="seats_num",
        ),
        migrations.AddField(
            model_name="contactusforenquires",
            name="slug",
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="letussellyourcar",
            name="attended_to",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="letussellyourcar",
            name="slug",
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="shipcarforussell",
            name="slug",
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="letussellyourcar",
            name="image_1",
            field=models.ImageField(blank=None, null=None, upload_to=None),
        ),
        migrations.AlterField(
            model_name="letussellyourcar",
            name="image_2",
            field=models.ImageField(blank=None, null=None, upload_to=None),
        ),
        migrations.AlterField(
            model_name="letussellyourcar",
            name="image_3",
            field=models.ImageField(blank=None, null=None, upload_to=None),
        ),
        migrations.AlterField(
            model_name="letussellyourcar",
            name="image_4",
            field=models.ImageField(blank=None, null=None, upload_to=None),
        ),
        migrations.AlterField(
            model_name="letussellyourcar",
            name="region",
            field=models.CharField(
                choices=[
                    ("VOLTA ", "VOLTA "),
                    ("BRONG AHAFO ", "BRONG AHAFO "),
                    ("OTI ", "OTI "),
                    ("CENTRAL ", "CENTRAL "),
                    ("EASTERN ", "EASTERN "),
                    ("GREATER ACCRA ", "GREATER ACCRA "),
                    ("NORTH EAST ", "NORTH EAST "),
                    ("NORTHERN ", "NORTHERN "),
                    ("SAVANNAH ", "SAVANNAH "),
                    ("UPPER EAST ", "UPPER EAST "),
                    ("UPPER WEST ", "UPPER WEST "),
                    ("WESTERN ", "WESTERN "),
                    ("WESTERN NORTH ", "WESTERN NORTH "),
                    ("BONO EAST  ", "BONO EAST  "),
                    ("AHAFO ", "AHAFO "),
                    ("ASHANTI ", "ASHANTI "),
                ],
                max_length=100,
            ),
        ),
        migrations.CreateModel(
            name="RentCar",
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
                ("name", models.CharField(max_length=200)),
                ("location", models.CharField(max_length=100)),
                ("contact", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                (
                    "region",
                    models.CharField(
                        choices=[
                            ("VOLTA ", "VOLTA "),
                            ("BRONG AHAFO ", "BRONG AHAFO "),
                            ("OTI ", "OTI "),
                            ("CENTRAL ", "CENTRAL "),
                            ("EASTERN ", "EASTERN "),
                            ("GREATER ACCRA ", "GREATER ACCRA "),
                            ("NORTH EAST ", "NORTH EAST "),
                            ("NORTHERN ", "NORTHERN "),
                            ("SAVANNAH ", "SAVANNAH "),
                            ("UPPER EAST ", "UPPER EAST "),
                            ("UPPER WEST ", "UPPER WEST "),
                            ("WESTERN ", "WESTERN "),
                            ("WESTERN NORTH ", "WESTERN NORTH "),
                            ("BONO EAST  ", "BONO EAST  "),
                            ("AHAFO ", "AHAFO "),
                            ("ASHANTI ", "ASHANTI "),
                        ],
                        max_length=100,
                    ),
                ),
                ("slug", models.SlugField(blank=True, editable=False, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("attended_to", models.BooleanField(default=False)),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="OurServices.carrental",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CarRentalImage",
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
                ("image", models.ImageField(upload_to=None)),
                ("slug", models.SlugField(blank=True, editable=False, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="OurServices.carrental",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
