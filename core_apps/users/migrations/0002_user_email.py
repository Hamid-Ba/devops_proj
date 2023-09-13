# Generated by Django 4.1 on 2023-09-13 19:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="email",
            field=models.EmailField(
                default="test@gmail.com",
                max_length=254,
                unique=True,
                verbose_name="email",
            ),
            preserve_default=False,
        ),
    ]
