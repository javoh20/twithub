from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView, name = 'main'),
    path('profile/', ProfileView, name = 'profile'),
    path('login/', LoginView, name = 'login'),
]
