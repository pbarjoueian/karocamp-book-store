# Generated by Django 4.2.11 on 2024-10-10 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="amount",
            field=models.IntegerField(default=1),
        ),
    ]