from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.
class User(AbstractUser):
    email = models.EmailField()


class Set(models.Model):
    name = models.CharField(max_length=128)
    color = models.CharField(max_length=7, default="f5f5dc")

    def __str__(self):
        return self.name


class Card(models.Model):
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    front = models.CharField(max_length=256)
    back = models.CharField(max_length=256)

    def __str__(self):
        return "(" + self.front + ", " + self.back + ")"


class Reflection(models.Model):
    body = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse("home")
