from django.http import *
from django.utils import simplejson

class JsonResponse(HttpResponse):
    """
    HttpResponse descendant, which return response with ``application/json`` mimetype.
    """
    def __init__(self, data):
        content = simplejson.dumps(data, encoding='utf-8')
        super(JsonResponse, self).__init__(content=content,
                                           mimetype='application/json; charset=utf-8')
