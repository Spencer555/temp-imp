# Generated by Django 4.1.3 on 2023-03-14 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Accessories", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="accessoriesimages",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="accessoriesenquiry",
            name="accessory",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="accessory_enquiry",
                to="Accessories.accessories",
            ),
        ),
        migrations.AddField(
            model_name="accessories",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
