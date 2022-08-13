from django.urls import path

from . import views

urlpatterns = [
    path('', views.initial),
    path('about', views.about),

]