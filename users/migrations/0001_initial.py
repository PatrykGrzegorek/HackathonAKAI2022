# Generated by Django 3.2.8 on 2022-11-04 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('surname', models.CharField(max_length=64, unique=True)),
                ('email', models.EmailField(max_length=64, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('type_of_account', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('profile_pic', models.FileField(blank=True, null=True, upload_to='prof_media')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
    ]
