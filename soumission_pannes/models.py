from django.db import models

class Infrastructure(models.Model):
    nom = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

class Panne(models.Model):
    infrastructure = models.ForeignKey(Infrastructure, on_delete=models.CASCADE, related_name='pannes')
    titre = models.CharField(max_length=255)
    description = models.TextField()
    date_signalement = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Non traitée', choices=[
        ('Non traitée', 'Non traitée'),
        ('En cours', 'En cours'),
        ('Résolue', 'Résolue'),
    ])

    def __str__(self):
        return f'{self.titre} - {self.infrastructure.nom}'
