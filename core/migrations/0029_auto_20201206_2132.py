# Generated by Django 3.1.1 on 2020-12-07 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20201124_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='filtering_fields',
        ),
        migrations.RemoveField(
            model_name='table',
            name='search_fields',
        ),
    ]