# Generated by Django 4.1.3 on 2023-04-05 09:22

import OurServices.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("OurServices", "0002_carrental_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carrental",
            name="car",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="carrental",
            name="contact_no",
            field=models.CharField(
                blank=True,
                max_length=17,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be entered in the format: '+233552229122'. Up to 15 digits allowed.",
                        regex="^\\+?1?\\d{9,15}$",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="carrental",
            name="main_image",
            field=models.ImageField(upload_to=OurServices.models.rental_path),
        ),
        migrations.AlterField(
            model_name="carrentalimage",
            name="image",
            field=models.ImageField(upload_to=OurServices.models.rental_images_path),
        ),
        migrations.AlterField(
            model_name="contactusforenquires",
            name="contact",
            field=models.CharField(
                blank=True,
                max_length=17,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be entered in the format: '+233552229122'. Up to 15 digits allowed.",
                        regex="^\\+?1?\\d{9,15}$",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="letussellyourcar",
            name="contact",
            field=models.CharField(
                blank=True,
                max_length=17,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be entered in the format: '+233552229122'. Up to 15 digits allowed.",
                        regex="^\\+?1?\\d{9,15}$",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="letussellyourcar",
            name="image_1",
            field=models.ImageField(
                blank=True, null=True, upload_to=OurServices.models.sell_images_path
            ),
        ),
        migrations.AlterField(
            model_name="letussellyourcar",
            name="image_2",
            field=models.ImageField(
                blank=True, null=True, upload_to=OurServices.models.sell_images_path
            ),
        ),
        migrations.AlterField(
            model_name="letussellyourcar",
            name="image_3",
            field=models.ImageField(
                blank=True, null=True, upload_to=OurServices.models.sell_images_path
            ),
        ),
        migrations.AlterField(
            model_name="letussellyourcar",
            name="image_4",
            field=models.ImageField(
                blank=True, null=True, upload_to=OurServices.models.sell_images_path
            ),
        ),
        migrations.AlterField(
            model_name="letussellyourcar",
            name="main_image",
            field=models.ImageField(upload_to=OurServices.models.sell_path),
        ),
        migrations.AlterField(
            model_name="letussellyourcar",
            name="year_manufactured",
            field=OurServices.models.YearField(max_length=4),
        ),
        migrations.AlterField(
            model_name="rentcar",
            name="contact",
            field=models.CharField(
                blank=True,
                max_length=17,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be entered in the format: '+233552229122'. Up to 15 digits allowed.",
                        regex="^\\+?1?\\d{9,15}$",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="shipcarforussell",
            name="contact",
            field=models.CharField(
                blank=True,
                max_length=17,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be entered in the format: '+233552229122'. Up to 15 digits allowed.",
                        regex="^\\+?1?\\d{9,15}$",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="shipcarforussell",
            name="image_1",
            field=models.ImageField(
                blank=True, null=True, upload_to=OurServices.models.ship_images_path
            ),
        ),
        migrations.AlterField(
            model_name="shipcarforussell",
            name="image_2",
            field=models.ImageField(
                blank=True, null=True, upload_to=OurServices.models.ship_images_path
            ),
        ),
        migrations.AlterField(
            model_name="shipcarforussell",
            name="image_3",
            field=models.ImageField(
                blank=True, null=True, upload_to=OurServices.models.ship_images_path
            ),
        ),
        migrations.AlterField(
            model_name="shipcarforussell",
            name="image_4",
            field=models.ImageField(
                blank=True, null=True, upload_to=OurServices.models.ship_images_path
            ),
        ),
        migrations.AlterField(
            model_name="shipcarforussell",
            name="main_image",
            field=models.ImageField(upload_to=OurServices.models.ship_path),
        ),
        migrations.AlterField(
            model_name="shipcarforussell",
            name="year_manufactured",
            field=OurServices.models.YearField(max_length=4),
        ),
    ]