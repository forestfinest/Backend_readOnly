from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):

    """User model."""
    username = None
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50, null=True)
    projects = models.CharField(null=True, max_length=200)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
