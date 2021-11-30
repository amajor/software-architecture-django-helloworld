from django.http import JsonResponse


def json_api(request):
    data = {
        'Message': 'Hello World!'
    }

    return JsonResponse(data, safe=False)
