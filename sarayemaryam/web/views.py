from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import *

# Create your views here.

@require_http_methods(['POST'])
@csrf_exempt
def register_user(request):
    context = {}

    if request.POST.get('username')\
    and request.POST.get('password')\
    and request.POST.get('phone'):
        context['status'] = 'ok'
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        User.objects.create(username=username, password=password, phone=phone)
        context['status'] = 'ok'
    return JsonResponse(context, encoder=JSONEncoder)
