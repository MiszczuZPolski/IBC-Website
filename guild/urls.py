from django.urls import path
from . import views

app_name = 'guild'

urlpatterns = [
    # Strona główna
    path('', views.home, name='home'),

    # O Nas
    path('about/', views.about, name='about'),

    # Kampanie
    path('campaigns/', views.campaign_list, name='campaign_list'),
    path('campaigns/<int:pk>/', views.campaign_detail, name='campaign_detail'),

    # Eventy

    #Kalendarz
    path('calendar/', views.calendar_view, name='calendar'),

    # Członkowie
    path('members/', views.member_list, name='member_list'),
    path('profile/', views.profile, name='profile'),

    # Galeria
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/upload/', views.gallery_upload, name='gallery_upload'),

    #Easter Egg
    path('easter-egg/', views.easter_egg, name='easter_egg'),
]
