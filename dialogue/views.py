from django.http import request
from django.shortcuts import render, get_object_or_404
from .models import Dialogue
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import DialogueForm

#login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# message class
from django.contrib.messages.views import SuccessMessageMixin

# http
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.


class DialogueListSpanishView(ListView):
    model = Dialogue
    template_name = "dialogue/dialogue.html"

    def get_queryset(self):
        user = self.request.user.id
        queryset = Dialogue.objects.filter(created_by=user).all()
        return queryset

class DialogueDetailView(LoginRequiredMixin, DetailView):
    model = Dialogue
    template_name = "dialogue/detail_dialogue.html"

    def get(self, request, *args, **kwargs):
        get_object_or_404(Dialogue, pk=kwargs['pk'], created_by=self.request.user)
        return super().get(request, *args, **kwargs)


class AddDialogueCreateView( LoginRequiredMixin,SuccessMessageMixin , CreateView):
    """ Para añadir un mensaje se utiliza el SuccesssMessageMixin y el atributo success_messages """
    permission_required = 'core.add_dialogue'
    form_class = DialogueForm
    template_name = "dialogue/add_dialogue.html"
    success_url = reverse_lazy('dialogue')
    success_message = 'Dialogo añadido correctamente'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class UpdateDialogueCreateView(LoginRequiredMixin, SuccessMessageMixin , UpdateView):
    """ Para añadir un mensaje se utiliza el SuccesssMessageMixin y el atributo success_messages """
    permission_required = 'dialogue.view_dialogue'
    model = Dialogue
    fields = ['spanish_dialogue', 'english_dialogue']
    template_name = "dialogue/update_dialogue.html"
    #success_url lo esta defiiendo el modelo Dialogue en models.py
    success_message = 'Dialogo modificado correctamente'


    def get(self, request, *args, **kwargs):
        get_object_or_404(Dialogue, pk=kwargs['pk'], created_by=self.request.user)
        return super().get(request, *args, **kwargs)


class DeleteDialogueView(LoginRequiredMixin, DeleteView):
    permission_required = 'dialogue.view_dialogue'
    model = Dialogue
    template_name = "dialogue/delete_dialogue.html"
    success_url = reverse_lazy('dialogue')


    def get(self, request, *args, **kwargs):
        get_object_or_404(Dialogue, pk=kwargs['pk'], created_by=self.request.user)
        return super().get(request, *args, **kwargs)
