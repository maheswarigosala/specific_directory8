from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return HttpResponse('<h1> 50 th century in ODI</h1>')
def shreyas(request):
    return HttpResponse('<h1> century in wc</h1>')
