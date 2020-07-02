# Generated by Django 2.1.5 on 2020-06-29 23:40

from api import validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapi',
            name='password',
            field=models.CharField(max_length=30, validators=[validators.validate_password_digit, validators.validate_password_uppercase]),
        ),
    ]