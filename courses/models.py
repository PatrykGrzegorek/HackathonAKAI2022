from django.db import models


class Answer(models.Model):
    answer = models.CharField(max_length=128)

    def __str__(self):
        return self.answer


class Question(models.Model):
    question = models.CharField(max_length=128)
    answers = models.ManyToManyField(Answer)

    def __str__(self):
        return self.question


class Game(models.Model):
    type = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=64)
    health = models.PositiveSmallIntegerField(default=0)
    monsters = models.PositiveSmallIntegerField(default=1)

    questions = models.ManyToManyField(Question)
