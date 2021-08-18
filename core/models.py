from django.utils import timezone
from core.manager import PhraseManager
from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from registration.models import Profile

from django.utils.text import slugify
# Create your models here.

class Phrase(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_phrase')
    spanish_phrase = models.CharField(verbose_name="Frase en español", max_length=200)
    english_phrase = models.CharField(verbose_name="Frase en ingles", max_length=200, 
                                        null=True, blank=True)
    learned = models.BooleanField(verbose_name="Frase aprendida?" , default=False)
    slug = models.SlugField(unique_for_date='publish', null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
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
        return reverse_lazy('detail_phrase', kwargs={'slug':self.slug, 'year':self.publish.year, 
                    'month':self.publish.month, 'day':self.publish.day, 'pk':self.pk})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.spanish_phrase)
        super().save(*args, **kwargs)

    