# Generated by Django 4.2.2 on 2023-06-26 00:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movie",
            old_name="user",
            new_name="added_by",
        ),
        migrations.AlterField(
            model_name="movie",
            name="duration",
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="movie",
            name="synopsis",
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
