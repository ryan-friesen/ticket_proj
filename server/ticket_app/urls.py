from django.urls import path
from . import views


# NO LEADING SLASHES
urlpatterns = [
    path('', views.index, name='index'),
    path('users/register', views.register, name='register'),
    path('users/dashboard', views.dashboard, name='dashboard'),
]
