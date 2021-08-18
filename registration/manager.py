from django.db import models

class ProfileManager(models.Manager):
    """ Manager para el modelo Phrase """
    

    def search_spanish(self, kword):
        resultado = self.filter(spanish_phrase__icontains=kword)
        return resultado
