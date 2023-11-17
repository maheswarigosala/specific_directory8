from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def williamson(request):
    return HttpResponse('<h1>williamson can score 50 in ODI</h1>')
def ravindra(request):
    return HttpResponse('<h1> youngstar </h1>')