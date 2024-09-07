from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    description = models.CharField(max_length = 255, null = True)
    photo = models.ImageField(upload_to = 'media/users/profile_photo', null = True)

class UserSubscribers(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='user')
    subscribers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers')
