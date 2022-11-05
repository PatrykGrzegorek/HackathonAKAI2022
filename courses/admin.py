from django.contrib import admin

from . import models


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'answer']


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']


@admin.register(models.Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
