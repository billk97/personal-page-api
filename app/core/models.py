from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


def validate_email(email):
    if not email:
        raise ValueError("Email can't be null")


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        validate_email(email)
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'