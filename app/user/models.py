from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group


class CatalogUserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, group, **extra_fields):
        """Private function to create user"""
        if not email:
            raise ValueError("The email is required")
        email = self.normalize_email(email)
        user = self.model.objects.create(email=email, **extra_fields)
        user.groups.add(group)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        raise ValueError("User creation is prohibited for this application.")

    def create_superuser(self, email, password, **extra_fields):
        """Creates a new superuser"""
        group, _ = Group.objects.get_or_create(name="Admin")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        user = self._create_user(email, password, group, **extra_fields)
        return user


class CatalogUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CatalogUserManager()

    def save(self, *args, **kwargs):
        self.username = self.email
        return super().save(*args, **kwargs)

    @property
    def roles(self):
        return self.groups
