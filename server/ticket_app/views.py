from django.shortcuts import render, redirect
from .models import User


def index(request):
    return render(request, "ticket_app/index.html")


def register(request):
    new_user = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=request.POST['password'],

    )
    print(new_user)
    return redirect("/users/dashboard")


def dashboard(request):
    context = {
        "all_users": User.objects.all()
    }
    return render(request, 'ticket_app/dashboard.html', context)
