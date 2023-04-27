# Generated by Django 4.1.3 on 2023-04-13 12:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Cars", "0004_alter_carenquiry_options_alter_carimage_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="contact_no",
            field=models.CharField(
                blank=True,
                max_length=17,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be entered in the format: '+999 999999999'. Up to 15 digits allowed.",
                        regex="^\\+?[0-9]{1,3}?\\s?\\-?[0-9]{1,15}$",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="carenquiry",
            name="contact_no",
            field=models.CharField(
                blank=True,
                max_length=17,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be entered in the format: '+999 999999999'. Up to 15 digits allowed.",
                        regex="^\\+?[0-9]{1,3}?\\s?\\-?[0-9]{1,15}$",
                    )
                ],
            ),
        ),
    ]
