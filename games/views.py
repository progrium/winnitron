from django.http import HttpResponse
from django.utils import simplejson
from games.models import Game
from games.utils import singularize

def xmlize(obj, parent='items'):
    if isinstance(obj, str):
        return obj
    elif isinstance(obj, dict):
        return ''.join(["<%s>%s</%s>" % (k, xmlize(obj[k], k), k) for k in obj])
    elif isinstance(obj, list):
        return ''.join(["<%s>%s</%s>" % (singularize(parent), xmlize(e), singularize(parent)) for e in obj])
    else:
        return str(obj)

def api_games(request, format):
    if format == 'json':
        return HttpResponse(simplejson.dumps({'games': [g.serialize() for g in Game.objects.all()]}))
    elif format == 'xml':
        return HttpResponse(xmlize({'games': [g.serialize() for g in Game.objects.all()]}))
    else:
        return HttpResponse("Unsupported format")
