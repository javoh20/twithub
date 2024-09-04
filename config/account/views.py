from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.views import View
from django.contrib.auth import authenticate, login



# Create your views here.
class RegisterUserView(View):
    template_name = 'signup.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('main')

        context = {
            'form': form
        }
        return render(request, self.template_name, context)
