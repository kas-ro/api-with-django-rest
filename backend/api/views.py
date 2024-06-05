import json

from django.shortcuts import render
from django.http import JsonResponse

def api_view(request):
    print(request.body)
    datas = json.loads(request.body)
    print(datas)
    print(request.headers)
    data = {
        "name": "rodrigue",
        "language": "python"
    }

    return JsonResponse(data)