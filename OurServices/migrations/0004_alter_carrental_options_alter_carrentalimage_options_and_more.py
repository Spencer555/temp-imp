# Generated by Django 4.1.3 on 2023-04-05 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("OurServices", "0003_alter_carrental_car_alter_carrental_contact_no_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="carrental",
            options={"verbose_name_plural": "Car Rentals"},
        ),
        migrations.AlterModelOptions(
            name="carrentalimage",
            options={"verbose_name_plural": "Car Rental Images"},
        ),
        migrations.AlterModelOptions(
            name="contactusforenquires",
            options={"verbose_name_plural": "Contact Us For Enquires"},
        ),
        migrations.AlterModelOptions(
            name="letussellyourcar",
            options={"verbose_name_plural": "Let Us Sell Your Car"},
        ),
        migrations.AlterModelOptions(
            name="shipcarforussell",
            options={"verbose_name_plural": "Ship Car For Us Sell"},
        ),
    ]
