# Generated by Django 4.2.2 on 2023-11-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("port1", "0002_info_alter_facts_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="projects",
            name="deploy_url",
            field=models.CharField(blank=True, max_length=99999999, null=True),
        ),
        migrations.AddField(
            model_name="projects",
            name="github_url",
            field=models.CharField(blank=True, max_length=99999999, null=True),
        ),
    ]
