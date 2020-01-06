from django.shortcuts import render, redirect


def index(request):
    return render(request, "ticket_app/index.html")


def register(request):
    return redirect("/users/dashboard")


def dashboard(request):
    return render(request, 'ticket_app/dashboard.html')
