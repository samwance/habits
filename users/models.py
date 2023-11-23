from django.contrib.auth.models import AbstractUser
from django.db import models

NULL = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='users/', blank=True, null=True)
    chat_id = models.PositiveIntegerField(**NULL)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
