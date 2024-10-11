from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import PanneForm, LoginForm, SignupForm  # Importez tous les formulaires nécessaires

# Vue pour soumettre une panne
def soumettre_panne(request):
    if request.method == 'POST':
        form = PanneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmation')  # Redirigez vers la vue de confirmation
    else:
        form = PanneForm()

    return render(request, 'soumission_pannes/soumettre.html', {'form': form})  # Ajustez le chemin ici

# Vue pour la confirmation
def confirmation(request):
    return render(request, 'soumission_pannes/confirmation.html')  # Page de confirmation

# Vue pour la page d'accueil (index)
def index(request):
    return render(request, 'soumission_pannes/index.html')

# Vue pour la connexion
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Authentification de l'utilisateur ici
            # Vous devez ajouter votre logique d'authentification
            return redirect('index')  # Redirigez vers la page d'accueil après connexion
    else:
        form = LoginForm()
    
    return render(request, 'soumission_pannes/login.html', {'form': form})

# Vue pour l'inscription
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Créer un nouvel utilisateur
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            
            return redirect('login')  # Redirigez vers la page de connexion
    else:
        form = SignupForm()

    return render(request, 'soumission_pannes/signup.html', {'form': form})

# Vue pour la page À propos
def a_propos_view(request):
    return render(request, 'soumission_pannes/a_propos.html')
