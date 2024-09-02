from django.shortcuts import render

# Create your views here.
def MainView(request):
    context = {}
    return render(request, 'index.html', context)

def ProfileView(request):
    context = {}
    return render(request, 'profile.html', context)

def LoginView(request):
    context = {}
    return render(request, 'login.html', context)