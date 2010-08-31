from django.http import HttpResponse
from django.utils import simplejson
from arcade.models import Game
from arcade.utils import singularize

def xmlize(obj, parent='items'):
    if isinstance(obj, str):
        return obj
    elif isinstance(obj, dict):
        return ''.join(["<%s>%s</%s>" % (k, xmlize(obj[k], k), k) for k in obj])
    elif isinstance(obj, list):
        return ''.join(["<%s>%s</%s>" % (singularize(parent), xmlize(e), singularize(parent)) for e in obj])
    elif obj == None:
        return ""
    else:
        return str(obj)

def api_games(request, format):
    data = {'games': [g.serialize() for g in Game.objects.all()]}
    if format == 'json':
        return HttpResponse(simplejson.dumps(data))
    elif format == 'xml':
        return HttpResponse(xmlize(data))
    else:
        return HttpResponse("Unsupported format")
