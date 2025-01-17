# Generated by Django 4.2.13 on 2024-06-29 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0002_remove_menuitem_imageurl_menuitem_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="PurchaseHistory",
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
                ("title", models.CharField(max_length=255)),
                ("imageUrl", models.URLField()),
                ("price", models.CharField(max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
