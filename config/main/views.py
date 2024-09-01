from django.shortcuts import render

# Create your views here.
def MainView(request):
    return render(request, 'index.html')

def ProfileView(request):
    return render(request, 'profile.html')

def LoginView(request):
    return render(request, 'login.html')