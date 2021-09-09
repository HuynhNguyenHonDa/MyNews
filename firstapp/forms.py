from django import forms
from django.forms import fields, widgets
from . models import AuthUser, StoriesStory, StoriesContact
import re
from django.contrib.auth.models import User

class StoriesStoryForm(forms.ModelForm):
     class Meta:
        model = StoriesStory
        fields = '__all__'
        # fields = ['name', 'author', 'url',  'content', 'category', 'image', ]
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control'}),
            'url' : forms.TextInput(attrs={'class': 'form-control'}),
            'content' : forms.TextInput(attrs={'class': 'form-control'}),
            # 'category' : forms.TextInput(attrs={'class': 'form-control'}),
            'image' : forms.FileInput(attrs={'class': 'form-control'}),
        }

class ContactForm(forms.ModelForm):
     class Meta:
        model = StoriesContact
        fields = '__all__'
        # widgets = {
        #     'name' : forms.TextInput(attrs={'class': 'form-control'}),
        #     'email' : forms.EmailInput(attrs={'class': 'form-control'}),
        #     'subject' : forms.TextInput(attrs={'class': 'form-control'}),
        #     'message' : forms.T(attrs={'class': 'textarea form-control'}),
        # }



