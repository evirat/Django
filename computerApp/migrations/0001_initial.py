# Generated by Django 4.2 on 2023-04-24 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Machine",
            fields=[
                (
                    "id",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("nom", models.CharField(max_length=200)),
            ],
        ),
    ]
