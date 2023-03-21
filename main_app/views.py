# Here we will be creating a class called Home and extending it from the View class

from django.urls import reverse
from django.views import View # <- View class to handle requests
from django.shortcuts import render
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
# import models
from .models import Artist
# from .models import ArtistCreate


# Home class, extending from the view class
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
    

# class ArtistCreate(CreateView):
#     model = Artist
#     fields = ['name', 'img', 'bio', 'verified_artist']
#     template_name = "artist_create.html"
#     success_url = "/artists/"
    
    
class ArtistDetail(DetailView):
    model = Artist
    template_name = "artist_detail.html"
    
# class ArtistUpdate(UpdateView):
#     model = Artist
#     fields = ['name', 'img', 'bio', 'verified_artist']
#     template_name = "artist_update.html"
#     success_url = "/artists/"
# # at the top of the file import reverse 

# ...


### **Modify success redirect to go to Artist Detail page**

# One bonus that would be nice, is if our redirects for create and update would go to the artist detail page. To do this we will be using a new method in our classes called get_success_url. For detailed info check out the docs.
class ArtistCreate(CreateView):
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = "artist_create.html"
    # this will get the pk from the route and redirect to artist view
    def get_success_url(self):
        return reverse('artist_detail', kwargs={'pk': self.object.pk})
        
        
class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = "artist_update.html"

    def get_success_url(self):
        return reverse('artist_detail', kwargs={'pk': self.object.pk})