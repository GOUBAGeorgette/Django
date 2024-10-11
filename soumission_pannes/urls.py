from django.urls import path
from .views import index, login_view, signup_view, soumettre_panne, confirmation, a_propos_view

urlpatterns = [
    path('', index, name='index'),  # Page d'accueil
    path('login/', login_view, name='login'),  # Vue pour la connexion
    path('signup/', signup_view, name='signup'),  # Vue pour l'inscription
    path('pannes/soumettre/', soumettre_panne, name='soumettre_panne'),  # Vue pour soumettre une panne
    path('pannes/confirmation/', confirmation, name='confirmation'),  # Vue de confirmation
    path('a_propos/', a_propos_view, name='a_propos'),  # Vue à propos
]

