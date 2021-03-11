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
    HtmlDefView,
    PythonDefView,
    IfView,
    ForView,
    WhileView,
    DictView,
)

urlpatterns = [
    path("", WelcomeView.as_view(), name="welcome"),
    path("home/", HomeView.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("pqa/", PythonView.as_view(), name="pqa"),
    path("print/", PrintView.as_view(), name="print"),
    path("indexes/", IndexView.as_view(), name="indexes"),
    path("if/",IfView.as_view(),name="if"),
    path("for/",ForView.as_view(),name="for"),
    path("while/",WhileView.as_view(),name="while"),
    path("dict/",DictView.as_view(),name="dict"),
    path("definitions/", DefinitionView.as_view(), name="definition"),
    path("htmldef/", HtmlDefView.as_view(), name="htmldef"),
    path("pythondef/", PythonDefView.as_view(), name="pydef"),
    path("reflections/", ReflectionCreateView.as_view(), name="reflection"),
]