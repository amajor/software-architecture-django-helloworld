from django.http import HttpResponse
from django.template import loader

from .models import Name


def index(request):
    template = loader.get_template('hello/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def person(request, name_id):
    return HttpResponse("Hello %s!" % Name.objects.get(id=name_id))
