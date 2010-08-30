from django.http import HttpResponse
from django.core import serializers
from winnitron.games.models import Game

def api_games(request, format):
    return HttpResponse(serializers.serialize(format, Game.objects.all()))
