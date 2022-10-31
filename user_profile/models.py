from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

# Create your models here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, name, phone, **extra_fields):
        if not email:
            raise ValueError('Email not provided')
        if not password:
            raise ValueError('Password not provided')

        user = self.model(
            email = self.normalize_email(email),
            name = name,
            phone = phone,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, name, phone, email_token, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, password, name, phone, email_token, **extra_fields)

    def create_superuser(self, email, password, name, phone, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, name, phone, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    phone = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email_token = models.CharField(max_length=1000, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone','email_token']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

def create_order(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        print('token generated')

post_save.connect(create_order, sender=User)