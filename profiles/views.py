from re import template
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponseRedirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from . forms import  RegistrationForm, loginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_ok')
    return render(request, 'profiles/register.html', {'form': form})

def register_ok(request):
    return render(request, 'profiles/register_ok.html')

# def loginUser(self, request ):
#     lF = loginForm()
#     if request.method == 'POST':
#         lF = loginForm(request.POST)
#         if lF.is_valid():
#             username = lF['username'].value()
#             password = lF['password'].value()
#             user = authenticate(request, username=username, password=password)
#             if username != User.objects.get('username'):
#                 raise lF.ValidationError("sai username")
#             elif password != User.objects.get('password'):
#                 raise lF.ValidationError('sai password')
#             elif user is not None:
#                 login(request, user)
#                 return render(request, 'firstapp/index.html')
#             else:
#                 return render(request, 'profiles/AccountLogin.html', {'lF': lF})
# class loginUser(View):
#     def get(self, request):
#         lF = loginForm
#         return render(request, 'profiles/AccountLogin.html', {'lF': lF})
#     def post(self, request):
#         lF = loginForm
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return render(request, '/firstapp/')
#         else:
#             return render(request, 'profiles/AccountLogin.html', {'lF': lF})