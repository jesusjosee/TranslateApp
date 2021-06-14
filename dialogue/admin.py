from django.contrib import admin
from .models import Dialogue
from core import models
# Register your models here.

@admin.register(Dialogue)
class DialogueAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    list_display = ['spanish_dialogue', 'english_dialogue', 'created']

