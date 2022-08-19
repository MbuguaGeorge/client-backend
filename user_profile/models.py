from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

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

    def create_user(self, email, name, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, name, phone, password, **extra_fields)

    def create_superuser(self, email, password, phone, name, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, phone, name, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    phone = models.CharField(max_length=200)
    name = models.CharField(max_length=255)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'