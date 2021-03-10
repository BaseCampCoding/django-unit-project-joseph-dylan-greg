from django.urls import path
from .views import (
    HomepageView,
    SignUpView,
    HomeView,
    PythonView,
    DefinitionView,
    ReflectionCreateView,
)

urlpatterns = [
    path("", HomepageView.as_view(), name="homepage"),
    path("home/", HomeView.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("pqa/", PythonView.as_view(), name="pqa"),
    path("definitions/", DefinitionView.as_view(), name="definition"),
    path("reflections/", ReflectionCreateView.as_view(), name="reflection"),
]