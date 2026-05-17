from django.contrib import admin
from django.urls import path
from stories import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('index/', views.home, name='index' ),
    path('info/', views.info,name='info'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('donate/', views.donate,name='donate'),
    path('stories/', views.stories,name='stories'),
    path('events/', views.events,name='events'),
    path('moreaboutus/', views.moreaboutus, name='moreaboutus')
    ]