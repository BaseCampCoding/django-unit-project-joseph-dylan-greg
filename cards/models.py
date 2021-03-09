from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField

# Create your models here.
class User(AbstractUser):
    email = models.EmailField()


# Question Model Code


class QuestionModel(models.Model):
    questions = ()
    Answer = MultiSelectField(choices=questions)
