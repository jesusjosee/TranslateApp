from django.shortcuts import render
from .models import Dialogue
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import DialogueForm

#login
from django.contrib.auth.mixins import PermissionRequiredMixin

# message class
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


class DialogueListSpanishView(ListView):
    model = Dialogue
    template_name = "dialogue/dialogue.html"

class DialogueDetailView(DetailView):
    model = Dialogue
    template_name = "dialogue/detail_dialogue.html"

class AddDialogueCreateView( PermissionRequiredMixin,SuccessMessageMixin , CreateView):
    """ Para añadir un mensaje se utiliza el SuccesssMessageMixin y el atributo success_messages """
    permission_required = 'core.add_dialogue'
    form_class = DialogueForm
    template_name = "dialogue/add_dialogue.html"
    success_url = reverse_lazy('dialogue')
    success_message = 'Dialogo añadido correctamente'

class UpdateDialogueCreateView(PermissionRequiredMixin, SuccessMessageMixin , UpdateView):
    """ Para añadir un mensaje se utiliza el SuccesssMessageMixin y el atributo success_messages """
    permission_required = 'dialogue.view_phrase'
    model = Dialogue
    fields = ['spanish_dialogue', 'english_dialogue']
    template_name = "dialogue/update_dialogue.html"
    #success_url lo esta defiiendo el modelo Dialogue en models.py
    success_message = 'Dialogo modificado correctamente'


class DeleteDialogueView(PermissionRequiredMixin, DeleteView):
    permission_required = 'dialogue.view_dialogue'
    model = Dialogue
    template_name = "dialogue/delete_dialogue.html"
    success_url = reverse_lazy('dialogue')