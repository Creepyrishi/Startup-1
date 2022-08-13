from django.shortcuts import render, HttpResponse

# Create your views here.
def initial(request):
    return render(request, 'home.html' )