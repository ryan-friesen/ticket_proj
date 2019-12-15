from django.urls import path
from . import views


# NO LEADING SLASHES
urlpatterns = [
    path('', views.index, name='index'),
    path('guest/<str:guest_name>', views.guest, name='guest'),

    path('tickets/<str:ticket_id>', views.ticket_info, name='ticket_info'),
]
