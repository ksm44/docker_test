from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def demo(request):
    return HttpResponse('OK')

@api_view(['GET'])
def demo_view(request):
    return Response({'status': 'OK', 'message': 'REST API работает'})
