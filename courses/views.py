from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView

from . import models
from . import serializers


@api_view(['GET'])
def OneGameView(request, id):
    try:
        if request.method == 'GET':
            queryset = models.Game.objects.get(id=id)
            list_answers = []
            list_questions = []
            for x in queryset.questions.all():
                for y in x.answers.all():
                    list_answers.append(y.answer)
                list_questions.append({"question": x.question, "answers": list_answers})
                list_answers = []
            dict_game = {"id": queryset.id, "type": queryset.type, "name": queryset.name, "questions":list_questions}
            return Response(dict_game, status=status.HTTP_200_OK)
    except models.Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def ListGameView(request):
    try:
        if request.method == 'GET':
            queryset = models.Game.objects.filter()
            list_games = []
            for x in queryset:
                list_games.append({"id": x.id, "name": x.name})
            dict_games = {"games": list_games}
            return Response(dict_games, status=status.HTTP_200_OK)
    except models.Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


