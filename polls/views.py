from django.shortcuts import render

from django.http import HttpResponse 

def index(request):
    return HttpResponse('Action creates mood. When in doubt - act! (polls index)')

# Create your views here. 
