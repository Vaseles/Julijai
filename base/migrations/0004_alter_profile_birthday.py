# Generated by Django 4.0.4 on 2022-07-11 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True),
        ),
    ]