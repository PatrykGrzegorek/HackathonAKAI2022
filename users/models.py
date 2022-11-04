from django.db import models


class LoginUser(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=32)


class CustomUser(models.Model):
    username = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, unique=True)
    password = models.CharField(max_length=32)
    type_of_account = models.PositiveSmallIntegerField(null=True, blank=True)
    profile_pic = models.FileField(upload_to="prof_media", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.username



