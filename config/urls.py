from django.contrib import admin
from django.urls import path, include
import cards.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("cards.urls")),
    path("videos/", cards.views.VideoView.as_view(), name="videos"),
]
