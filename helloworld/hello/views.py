import requests
from django.shortcuts import render

from .models import Name


def index(request):
    res = requests.get(f"http://127.0.0.1:8000/api/")
    json_response = res.json()
    context = {
        'response': json_response,
    }
    return render(request, 'hello/index.html', context)


def person(request, name_id):
    context = {
        'name': Name.objects.get(id=name_id),
    }
    return render(request, 'hello/person.html', context)
