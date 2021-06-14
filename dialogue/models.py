from core.manager import PhraseManager
from django.db import models
from django.urls import reverse_lazy
# Create your models here.

class Dialogue(models.Model):
    spanish_dialogue = models.TextField(verbose_name="Dialogo en español")
    english_dialogue = models.TextField(verbose_name="Dialogo en ingles", 
                                        null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    objects = PhraseManager()

    class Meta:
        ordering = ['-created']
        verbose_name = "Dialogo"
        verbose_name_plural = "Dialogos"

    def __str__(self):
        return self.spanish_dialogue
    

    def get_absolute_url(self):
        return reverse_lazy('detail_dialogue', kwargs={'pk': self.pk})