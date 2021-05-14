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
    """ this function for register user with API
    """
    context = {}

    if request.POST.get('username')\
    and request.POST.get('password')\
    and request.POST.get('phone'):

        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')

        users_list = User.objects.filter(username = username)
        phones_list = User.objects.filter(phone = phone)

        if users_list:
            context['status'] = 'error'
            context['message'] = 'Duplicate username'
        else:
            if phones_list:
                context['status'] = 'error'
                context['message'] = 'Duplicate phone'
            else:
                User.bojects.create(username=username, password=password, phone=phone)

                context['status'] = 'ok'
                context['username'] = username
                context['password'] = password
                context['phone'] = phone
    return JsonResponse(context, encoder=JSONEncoder)


@require_http_methods(['POST'])
@csrf_exempt
def login_user(request):
    """ this function for check username with password and return user info
    """

    context = {}

    if request.POST.get('username')\
    and request.POST.get('password'):

        username = request.POST.get('username')
        password = request.POST.get('password')
        
        users_list = User.objects.filter(username = username, password = password)

        if users_list:
            user = User.objects.filter(username = username, password = password).get()

            context['status'] = 'ok'

            context['username'] = user.username
            context['phone'] = user.password
            context['address'] = user.address
            context['post_code'] = user.post_code

            return JsonResponse(context, encoder=JSONEncoder)
        else:
            context['status'] = 'error'
            context['meessage'] = 'username or password is wrong'

            return JsonResponse(context, encoder=JSONEncoder)
