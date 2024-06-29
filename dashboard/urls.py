from django.urls import path, re_path
from .views import home, about


urlpatterns = [
    path('', home, name="home"),
    path('about', about, name="about")
]