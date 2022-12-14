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
        dat.thumbnail = item['fields']['Thumbnail']
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
            dat.thumbnail = item['fields']['Thumbnail']
            
            dat.description = f'<!DOCTYPE html><html lang="en" style="font-size:10px; color:white"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head><body>{item["fields"]["Description"]}</body></html>'
            
            return render(request, "service.html", {'dat':dat})

    else:
        return render(request, "message.html", {'message': 'DATA NOT FOUND'})


    
    