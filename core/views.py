from django.contrib.messages.api import get_messages
from django.db.models import query
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Phrase
from .forms import PhraseForm
from django.urls import reverse_lazy, reverse

# message class
from django.contrib.messages.views import SuccessMessageMixin

#login 
from .forms import CustomUserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
# Create your views here.


class PhraseListSpanishView(ListView):
    model = Phrase
    template_name = "core/list_all_spanish_phrase.html"
    paginate_by = 10

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        queryset = Phrase.objects.search_spanish(palabra_clave)
        return queryset

class PhraseListEnglishView(ListView):
    model = Phrase
    template_name = "core/list_all_english_phrase.html"
    paginate_by = 10

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        queryset = Phrase.objects.search_english(palabra_clave)
        return queryset

class PhraseDetailView(DetailView):
    model = Phrase
    template_name = "core/detail_phrase.html"
       
    
class AddPhraseCreateView( PermissionRequiredMixin,SuccessMessageMixin , CreateView):
    """ Para añadir un mensaje se utiliza el SuccesssMessageMixin y el atributo success_messages """
    permission_required = 'core.add_phrase'
    form_class = PhraseForm
    template_name = "core/add_phrase.html"
    success_url = reverse_lazy('home')
    success_message = 'Frase añadida correctamente'

class UpdatePhraseCreateView(PermissionRequiredMixin, SuccessMessageMixin , UpdateView):
    """ Para añadir un mensaje se utiliza el SuccesssMessageMixin y el atributo success_messages """
    permission_required = 'core.view_phrase'
    model = Phrase
    fields = ['spanish_phrase', 'english_phrase', 'learned']
    template_name = "core/update_phrase.html"
    #success_url lo esta defiiendo el modelo Phrase en models.py
    success_message = 'Frase modificada correctamente'


class DeletePhraseView(PermissionRequiredMixin, DeleteView):
    permission_required = 'core.view_phrase'
    model = Phrase
    template_name = "core/delete_phrase.html"
    success_url = reverse_lazy('home')


class LearnedListView(PermissionRequiredMixin, ListView):
    permission_required = 'core.view_phrase'
    model = Phrase
    template_name = "core/list_learned.html"

    def get_queryset(self):
        queryset = Phrase.objects.learned_phrase()
        return queryset


class NoLearnedListView(PermissionRequiredMixin, ListView):
    permission_required = 'core.view_phrase'
    model = Phrase
    template_name = "core/list_nolearned.html"

    def get_queryset(self):
        queryset = Phrase.objects.nolearned_phrase()
        return queryset

class LearnedEnglishListView(PermissionRequiredMixin, ListView):
    permission_required = 'core.view_phrase'
    model = Phrase
    template_name = "core/list_learned_english.html"

    def get_queryset(self):
        queryset = Phrase.objects.learned_phrase_english()
        return queryset


class NoLearnedEnglishListView(PermissionRequiredMixin, ListView):
    permission_required = 'core.view_phrase'
    model = Phrase
    template_name = "core/list_nolearned_english.html"

    def get_queryset(self):
        queryset = Phrase.objects.nolearned_phrase_english()
        return queryset

class NoEditListView(PermissionRequiredMixin, ListView):
    permission_required = 'core.view_phrase'
    model = Phrase
    template_name = "core/no_edit.html"

    def get_queryset(self):
        queryset = Phrase.objects.no_edit()
        print(queryset)
        return queryset

def registration(request):

    data = {'form' : CustomUserCreationForm()}

    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            cd = form.cleaned_data
            #authenticar y logear
            user = authenticate(username=cd['username'], password=cd['password1'])
            login(request, user)
            #mensaje
            messages.success(request, "Te has registrado correctamente")
            #redirige
            return redirect('/')


    return render(request, 'registration/sign-up.html', data)