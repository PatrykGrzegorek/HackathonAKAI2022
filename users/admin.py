from django.contrib import admin

from . import models


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'username', 'name', 'surname', 'created']
    list_filter = ['username', 'email', 'created']

