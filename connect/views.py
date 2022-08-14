from django.shortcuts import render, HttpResponse
from db import addMessage

# Create your views here.
def connect(request):
    if request.method == 'POST':
        
        firstName = request.POST.get("first-name")
        lastName = request.POST.get("last-name")
        fullName = firstName + " " + lastName
        email = request.POST.get("email")
        phoneNumber = request.POST.get("Phone-number")
        message = request.POST.get("Message")
        
        # adding message in airtable 
        if addMessage(name=fullName, phone=phoneNumber, mail=email , message=message):
            return render(request, "message.html", {'message': f'{fullName} your request has been sucess fully submitted'})
        else:
            return render(request, "message.html", {'message': f'{fullName} something went wrong'})
