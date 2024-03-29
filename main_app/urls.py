from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('artists/', views.ArtistList.as_view(), name="artist_list"),
    path('artists/new', views.ArtistCreate.as_view(), name="artist_create"),
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name="artist_detail"),
    path('artists/<int:pk>/update',
         views.ArtistUpdate.as_view(), name="artist_update"),
    # Our new Route including the pk param
    path('artists/<int:pk>/delete',views.ArtistDelete.as_view(), name="artist_delete"),
]