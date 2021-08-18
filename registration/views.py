from django.contrib.auth.models import User
from registration.models import Profile
from django.http import request
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView, UpdateView
from .forms import SignUpForm
from django.urls import reverse_lazy

#autenticacion
from django.contrib.auth import login, authenticate

#permisos
from django.contrib.auth.mixins import LoginRequiredMixin

#messages funciontion
from django.contrib import messages

# framework message class
from django.contrib.messages.views import SuccessMessageMixin

#ESTA VISTA SE DEBE COLOCAR EL LOGIN_REQUIRED
# class ProfiLeView(LoginRequiredMixin ,TemplateView):
#     login_url = '/login/'
#     template_name = "registration/perfil.html"

class ProfiLeView(LoginRequiredMixin, SuccessMessageMixin ,UpdateView):
    login_url = '/login/'
    template_name = "registration/perfil.html"
    model = Profile
    fields = ['avatar', 'biografia']
    success_url = reverse_lazy('profile')
    success_message = 'Perfil actualizado satisfactoriamente'
    
    #crear un perfil en caso no exista
    def get_object(self) :
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

class SignUp(CreateView):
    template_name = "registration/signup.html"
    form_class = SignUpForm
    
    #logear un usuario despues de registrarlo
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password1'])
            login(request, user)
            messages.success(request,'Usuario creado satisfactoriamente')
            return redirect('profile')
        return super().post(request, *args, **kwargs)

  