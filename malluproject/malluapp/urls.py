from django.urls import path
from malluapp import views

urlpatterns = [
    path('', views.demo, name='demo'),
    path('about.html/', views.about, name='about'),
    path('Contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('Home.html/', views.Home, name='Home.html')
    # path('about.html/Home.html/', views.Home, name='Home'),
]