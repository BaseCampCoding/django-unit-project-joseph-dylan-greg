from django.urls import path
from .views import HomepageView, SignUpView,HomeView,PythonView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('home/',HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('pqa/',PythonView.as_view(), name='pqa')
]