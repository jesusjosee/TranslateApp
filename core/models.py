from core.manager import PhraseManager
from django.db import models
from django.urls import reverse_lazy
# Create your models here.

class Phrase(models.Model):
    spanish_phrase = models.CharField(verbose_name="Frase en español", max_length=200)
    english_phrase = models.CharField(verbose_name="Frase en ingles", max_length=200, 
                                        null=True, blank=True)
    learned = models.BooleanField(verbose_name="Frase aprendida?" , default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    objects = PhraseManager()

    class Meta:
        ordering = ['-created']
        verbose_name = "Frase"
        verbose_name_plural = "Frases"

    def __str__(self):
        return self.spanish_phrase
    

    def get_absolute_url(self):
        return reverse_lazy('detail_phrase', kwargs={'pk': self.pk})