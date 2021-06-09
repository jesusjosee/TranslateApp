from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Phrase
from core import models
# Register your models here.

@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    list_display = ['spanish_phrase', 'english_phrase', 'created', 'learned']

