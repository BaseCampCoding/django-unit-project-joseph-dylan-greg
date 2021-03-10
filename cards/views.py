from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Reflection

# Create your views here.
class WelcomeView(TemplateView):
    template_name = "homepage.html"


class HomeView(TemplateView):
    template_name = "home.html"


class ReflectionCreateView(CreateView):
    template_name = "reflections.html"
    model = Reflection
    fields = ("body",)


class DefinitionView(TemplateView):
    template_name = "defintion.html"


class VideoView(TemplateView):
    template_name = "videos.html"


# question templates
class PythonView(TemplateView):
    template_name = "pqa.html"


class PrintView(TemplateView):
    template_name = "print.html"


class IndexView(TemplateView):
    template_name = "Indexes.html"


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
