from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# creating navbar,or the lookout

def home(request):
    return HttpResponse("<h1>Blog home</h1>")

#view=url(all view need url)

def about(request):
    return HttpResponse("<h1>Blog house</h1>")

