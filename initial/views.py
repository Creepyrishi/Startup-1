from dataclasses import dataclass
from django.shortcuts import render, HttpResponse
from .models import data
from db import getServices

# Create your views here.
def initial(request):
    services = []
    for item in getServices():
        dat = data()
        dat.id = item['id']
        dat.title = item['fields']['Title']
        dat.description = item['fields']['Description']
        services.append(dat)

    return render(request, "home.html", {'services' : services})


def about(request):
    return render(request, "about.html")

def service(request, id):

    for item in getServices():
        if item['id'] == id:
            dat = data()
            dat.id = item['id']
            dat.title = item['fields']['Title']
            dat.description = item['fields']['Description']
            
            return render(request, "service.html", {'dat':dat})

    else:
        return HttpResponse("<h2>DATA NOT FOUND</h2>")

    
    