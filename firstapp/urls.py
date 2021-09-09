from django.urls import path
from . import views
from django.conf.urls import url

# app_name = 'firstapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('Blog/', views.Blog, name='blog'),
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('contact_ok/', views.contact_ok, name='contact_ok'),
    path('Acticle/', views.Acticle, name='acticle'),
    path('single/<int:id>', views.Blogdetails, name='single'),
    path('quanTriduLieu/', views.quanTriduLieu, name='quanTriduLieu'),
    path('addStoriesStory/', views.addStoriesStory, name='addStoriesStory'),
    path('editStoriesStory/<str:pk>/', views.editStoriesStory, name='editStoriesStory'),
    path('deleteStoriesStory/<str:pk>/', views.deleteStoriesStory, name='deleteStoriesStory'),
]