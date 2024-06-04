from django.shortcuts import render
from django.http import JsonResponse

def api_view(request):
    data = {
        "name": "rodrigue",
        "language": "python"
    }

    return JsonResponse(data)