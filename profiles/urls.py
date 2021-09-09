from profiles import views
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
     path('register/', views.register, name="register"),
     path('register_ok/', views.register_ok, name="register_ok"),
     path('', include('firstapp.urls'), name='firstapp'),
     path('loginUser', auth_views.LoginView.as_view(template_name="profiles/AccountLogin.html"), name="loginUser"),
     path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
     path('login/',auth_views.LoginView.as_view(template_name="profiles/AccountLogin.html"), name="login"),
]