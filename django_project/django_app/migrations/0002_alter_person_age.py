# Generated by Django 4.2.14 on 2024-08-05 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="Age",
            field=models.IntegerField(max_length=3),
        ),
    ]
