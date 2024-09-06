from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def MainView(request):
    context = {}
    return render(request, 'index.html', context)

@login_required
def ProfileView(request):
    user = User.objects.get(user = request.user)
    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)

def LoginView(request):
    context = {}
    return render(request, 'login.html', context)