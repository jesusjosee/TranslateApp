from django import forms
from django.db import models
from django.forms import fields
from .models import Phrase

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PhraseForm(forms.ModelForm):

    class Meta:
        model = Phrase
        fields = ['spanish_phrase', 'english_phrase']

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']