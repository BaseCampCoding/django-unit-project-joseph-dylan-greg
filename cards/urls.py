from django.urls import path
from .views import HomepageView, SignUpView,HomeView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('home/',HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
]