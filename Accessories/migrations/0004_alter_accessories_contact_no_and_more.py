# Generated by Django 4.1.3 on 2023-04-05 09:22

import Accessories.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Accessories", "0003_accessoriesenquiry_attended_to"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accessories",
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
            model_name="accessories",
            name="main_image",
            field=models.ImageField(upload_to=Accessories.models.accessories_path),
        ),
        migrations.AlterField(
            model_name="accessoriesenquiry",
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
            model_name="accessoriesimages",
            name="image",
            field=models.ImageField(
                upload_to=Accessories.models.accessories_images_path
            ),
        ),
    ]