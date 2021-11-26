from django.http import HttpResponse

from .models import Name


def index(request):
    return HttpResponse("Hello world!")


def person(request, name_id):
    return HttpResponse("Hello %s!" % Name.objects.get(id=name_id))
