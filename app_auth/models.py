from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from utilitas.models import BaseModel
from app_auth.managers import CustomUserManager


# Create your models here.
class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    """
    The user model
    """

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=512)
    groups = None
    user_permissions = None

    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    def __str__(self):
        return f"<User: {self.id} {self.email}>"

    class Meta:
        ordering = ("id",)
