from django.db import models

class Panne(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    localisation = models.CharField(max_length=200)

    def __str__(self):
        return self.titre
