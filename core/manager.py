from django.db import models

class PhraseManager(models.Manager):
    """ Manager para el modelo Phrase """
    def learned_phrase(self):
        resultado = self.filter(learned=True)
        return resultado

    def nolearned_phrase(self):
        resultado = self.filter(learned=False)
        return resultado

    def learned_phrase_english(self):
        resultado = self.filter(learned=True)
        return resultado

    def nolearned_phrase_english(self):
        resultado = self.filter(learned=False)
        return resultado

    def no_edit(self):
        resultado = self.filter(english_phrase__iexact=None)
        return resultado

    def search_spanish(self, kword):
        resultado = self.filter(spanish_phrase__icontains=kword)
        return resultado


    def search_english(self, kword):
        resultado = self.filter(english_phrase__icontains=kword)
        return resultado