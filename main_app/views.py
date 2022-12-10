# Here we will be creating a class called Home and extending it from the View class

from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView

# GET request
class Home(View):
    def get(self, request):
        return HttpResponse("Spotify Home") #similar to res.send()


class About(View):
    def get(self, request):
        return HttpResponse("Spotify About")