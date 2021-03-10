from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class HomepageView(TemplateView):
    template_name = "homepage.html"


class HomeView(TemplateView):
    template_name = "home.html"


class VideoView(TemplateView):
    template_name = "videos.html"


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
