# Generated by Django 4.2 on 2023-05-03 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0002_snack_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='snack',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]