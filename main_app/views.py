# Here we will be creating a class called Home and extending it from the View class

from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
# import models
from .models import Artist


# GET request
class Home(View):
    def get(self, request):
        return HttpResponse("Spotify Home") #similar to res.send()


class About(View):
    def get(self, request):
        return HttpResponse("Spotify About")
    

class Home(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about.html"
    
    

class ArtistList(TemplateView):
    template_name = "artist_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #method passes data to template
        context["artists"] = Artist.objects.all() # Here we are using the model to query the database for us.
        return context