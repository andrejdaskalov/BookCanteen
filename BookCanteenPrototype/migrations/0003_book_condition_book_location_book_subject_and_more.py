# Generated by Django 4.2.2 on 2023-06-21 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("BookCanteenPrototype", "0002_book_new"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="condition",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="book",
            name="location",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="book",
            name="subject",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="bookuser", name="rating", field=models.FloatField(default=0),
        ),
    ]