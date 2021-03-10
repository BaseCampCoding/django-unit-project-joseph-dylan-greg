from django.urls import path
from .views import (
    WelcomeView,
    SignUpView,
    HomeView,
    PythonView,
    DefinitionView,
    ReflectionCreateView,
    PrintView,
    IndexView,
    PythonDefView,
)

urlpatterns = [
    path("", WelcomeView.as_view(), name="welcome"),
    path("home/", HomeView.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("pqa/", PythonView.as_view(), name="pqa"),
    path("print/", PrintView.as_view(), name="print"),
    path("indexes/", IndexView.as_view(), name="indexes"),
    path("definitions/", DefinitionView.as_view(), name="definition"),
    path("pythondef/", PythonDefView.as_view(), name="pydef"),
    path("reflections/", ReflectionCreateView.as_view(), name="reflection"),
]