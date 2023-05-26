# Generated by Django 4.2 on 2023-05-26 07:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0012_alter_machine_maintenancedate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 5, 26, 7, 32, 4, 788344)
            ),
        ),
        migrations.CreateModel(
            name="Infrastructure",
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
                ("nom_infra", models.CharField(max_length=200)),
                ("machines", models.ManyToManyField(to="computerApp.machine")),
            ],
        ),
    ]
