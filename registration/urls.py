from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.ProfiLeView.as_view(), name='profile'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]