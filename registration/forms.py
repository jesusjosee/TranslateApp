from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True,
             help_text='Requerido, 254 caracteres como máximo, debe ser un email válido')

    class Meta:
        model = User
        fields = ('username','first_name' ,'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email ya esta registrado, prueba con otro')

        return email