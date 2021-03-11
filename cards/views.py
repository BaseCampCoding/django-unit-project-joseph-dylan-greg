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

# Definition templates
class DefinitionView(TemplateView):
    template_name = "definition.html"

class PythonDefView(TemplateView):
    template_name = "python_def.html"

class HtmlDefView(TemplateView):
    template_name = "html_def.html"

#Video templates
class VideoView(TemplateView):
    template_name = "videos.html"

# question templates
class PythonView(TemplateView):
    template_name = "questions/pqa.html"

class PrintView(TemplateView):
    template_name = "questions/print.html"

class IndexView(TemplateView):
    template_name = "questions/indexes.html"

class IfView(TemplateView):
    template_name="questions/if.html"

class ForView(TemplateView):
    template_name="questions/for.html"

class WhileView(TemplateView):
    template_name="questions/while.html"

class DictView(TemplateView):
    template_name="questions/dict.html"


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
