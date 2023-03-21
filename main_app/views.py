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
         # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            context["artists"] = Artist.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["artists"] = Artist.objects.all()
            # default header for not searching 
            context["header"] = f"Searching for {name}"
        return context