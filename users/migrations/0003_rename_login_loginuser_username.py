# Generated by Django 3.2.8 on 2022-11-04 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_email_loginuser_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loginuser',
            old_name='login',
            new_name='username',
        ),
    ]
