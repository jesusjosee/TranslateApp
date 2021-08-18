from core.manager import PhraseManager
from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.utils import timezone

from django.contrib.auth.models import User
# Create your models here.

class Dialogue(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_dialogue')
    spanish_dialogue = models.TextField(verbose_name="Dialogo en español")
    english_dialogue = models.TextField(verbose_name="Dialogo en ingles", 
                                        null=True, blank=True)
    slug = models.SlugField(unique_for_date='publish', null=True, blank=True)
    publish= models.DateTimeField(default=timezone.now)
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
        return reverse_lazy('detail_dialogue', 
                    kwargs={'slug':self.slug, 'year':self.publish.year, 
                    'month':self.publish.month, 'day':self.publish.day, 'pk':self.pk})

    def save(self, *args, **kwargs):
        self.slug= slugify(self.spanish_dialogue)
        super().save(*args, **kwargs)