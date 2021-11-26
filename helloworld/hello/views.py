from django.shortcuts import render

from .models import Name


def index(request):
    context = {}
    return render(request, 'hello/index.html', context)


def person(request, name_id):
    context = {
        'name': Name.objects.get(id=name_id),
    }
    return render(request, 'hello/person.html', context)
