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