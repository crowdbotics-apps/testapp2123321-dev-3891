# Generated by Django 2.2.12 on 2020-04-30 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_load_initial_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="customtext",
            name="test",
            field=models.OneToOneField(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="customtext_test",
                to="home.CustomText",
            ),
        ),
    ]
