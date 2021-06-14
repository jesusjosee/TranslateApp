from django import forms
from .models import Dialogue

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DialogueForm(forms.ModelForm):

    class Meta:
        model = Dialogue
        fields = ['spanish_dialogue', 'english_dialogue']
