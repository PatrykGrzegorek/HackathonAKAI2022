# Generated by Django 3.2.8 on 2022-11-04 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_login_loginuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='surname',
            field=models.CharField(max_length=64),
        ),
    ]
