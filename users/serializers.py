from rest_framework import serializers

from . import models


class LoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.LoginUser
        fields = '__all__'


class CustomUserSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(write_only=False, required=False)

    class Meta:
        model = models.CustomUser
        fields = ['id', 'username', 'name', 'surname', 'cash', 'email', 'type_of_account', 'profile_pic', 'created']


class CustomUserRegistrationSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = ['username', 'name', 'surname', 'email', 'password', 'type_of_account', 'profile_pic', 'created']


class AddCash(serializers.ModelSerializer):

    class Meta:
        model = models.Cash
        fields = ['cash']