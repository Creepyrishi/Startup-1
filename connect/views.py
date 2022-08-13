from django.shortcuts import render, HttpResponse

# Create your views here.
def connect(request):
    return HttpResponse("hello there")