from django.contrib.messages.api import get_messages
from django.db import models
from django.db.models import query
from django.http import request
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Phrase
from .forms import PhraseForm
from django.urls import reverse_lazy, reverse
from registration.models import Profile
from django.contrib.auth.models import User

# message class
from django.contrib.messages.views import SuccessMessageMixin

#login 
from .forms import CustomUserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
# Create your views here.

class PhraseListSpanishView(ListView):
    model = Phrase
    template_name = "core/list_all_spanish_phrase.html"
    paginate_by = 10

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        user=self.request.user.id
        queryset = Phrase.objects.search_spanish(palabra_clave).filter(created_by=user)
        return queryset

class PhraseListEnglishView(ListView):
    model = Phrase
    template_name = "core/list_all_english_phrase.html"
    paginate_by = 10

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        user=self.request.user.id
        queryset = Phrase.objects.search_english(palabra_clave).filter(created_by=user)
        return queryset

class PhraseDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = Phrase
    template_name = "core/detail_phrase.html"

    # def get(self, request, *args, **kwargs):
    #     get_object_or_404(Phrase, pk=kwargs['pk'], created_by=self.request.user)
    #     return super().get(request, *args, **kwargs)
       
    def get_queryset(self):
        queryset = Phrase.objects.filter(pk=self.kwargs['pk'], created_by=self.request.user)
        return queryset
    
class AddPhraseCreateView( LoginRequiredMixin,SuccessMessageMixin , CreateView):
    """ Para añadir un mensaje se utiliza el SuccesssMessageMixin y el atributo success_messages """
    #permission_required = 'core.add_phrase'
    login_url = '/login/'
    form_class = PhraseForm
    template_name = "core/add_phrase.html"
    success_url = reverse_lazy('home')
    success_message = 'Frase añadida correctamente'
    #redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class UpdatePhraseCreateView(LoginRequiredMixin, SuccessMessageMixin , UpdateView):
    """ Para añadir un mensaje se utiliza el SuccesssMessageMixin y el atributo success_messages """
    login_url = '/login/'
    permission_required = 'core.view_phrase'
    model = Phrase
    fields = ['spanish_phrase', 'english_phrase', 'learned']
    template_name = "core/update_phrase.html"
    #success_url lo esta defiiendo el modelo Phrase en models.py
    success_message = 'Frase modificada correctamente'

    def get(self, request, *args, **kwargs):
        get_object_or_404(Phrase, pk=kwargs['pk'], created_by=self.request.user)
        return super().get(request, *args, **kwargs)


class DeletePhraseView(LoginRequiredMixin, DeleteView):
    
    #permission_required = 'core.view_phrase'
    login_url = '/login/'
    model = Phrase
    template_name = "core/delete_phrase.html"
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        get_object_or_404(Phrase, pk=kwargs['pk'], created_by=self.request.user)
        return super().get(request, *args, **kwargs)

class LearnedListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    #permission_required = 'core.view_phrase'
    model = Phrase
    template_name = "core/list_learned.html"

    def get_queryset(self):
        user=self.request.user.id
        queryset = Phrase.objects.learned_phrase().filter(created_by=user)
        return queryset


class NoLearnedListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    #permission_required = 'core.view_phrase'
    model = Phrase
    template_name = "core/list_nolearned.html"

    def get_queryset(self):
        user=self.request.user.id
        queryset = Phrase.objects.nolearned_phrase().filter(created_by=user)
        return queryset

class LearnedEnglishListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    #permission_required = 'core.view_phrase'
    model = Phrase
    template_name = "core/list_learned_english.html"

    def get_queryset(self):
        user=self.request.user.id
        queryset = Phrase.objects.learned_phrase_english().filter(created_by=user)
        return queryset


class NoLearnedEnglishListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    #permission_required = 'core.view_phrase'
    model = Phrase
    template_name = "core/list_nolearned_english.html"

    def get_queryset(self):
        user=self.request.user.id
        queryset = Phrase.objects.nolearned_phrase_english().filter(created_by=user)
        return queryset

class NoEditListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    #permission_required = 'core.view_phrase'
    model = Phrase
    template_name = "core/no_edit.html"

    def get_queryset(self):
        user=self.request.user.id
        queryset = Phrase.objects.no_edit().filter(created_by=user)
        print(queryset)
        return queryset

# def registration(request):

#     data = {'form' : CustomUserCreationForm()}

#     if request.method == 'POST':
#         form = CustomUserCreationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             cd = form.cleaned_data
#             #authenticar y logear
#             user = authenticate(username=cd['username'], password=cd['password1'])
#             login(request, user)
#             #mensaje
#             messages.success(request, "Te has registrado correctamente")
#             #redirige
#             return redirect('/')


#     return render(request, 'registration/sign-up.html', data)



class Pruebaquery(ListView):
    model = Phrase
    template_name = "core/prueba-all-phrase-spanish.html"
    paginate_by = 10

    def get_queryset(self):
        user= self.request.user.id
        palabra_clave = self.request.GET.get('kword', '')
        queryset = Phrase.objects.search_spanish(palabra_clave).filter(created_by=user)
        return queryset