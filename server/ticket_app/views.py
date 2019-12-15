from django.shortcuts import render, redirect
import uuid

all_tickets = [
    {
        'id': uuid.uuid4().hex,
        'submitted_by': 'Ryan',
        'title': 'POS System Down',
        'description': 'The POS system is down',
    },
    {
        'id': uuid.uuid4().hex,
        'submitted_by': 'Ryan',
        'title': 'Register offline',
        'description': 'The register says register is offline! Please advise.',
    },
]


def index(request):

    context = {
        'msg': 'hello client!',
        'tickets': all_tickets
    }

    return render(request, 'index.html', context)


def guest(request, guest_name):

    context = {
        'guest': guest_name
    }

    return render(request, 'guest.html', context)


def ticket_info(request, ticket_id):

    selected_ticket = None

    for ticket in all_tickets:
        if ticket['id'] == ticket_id:
            selected_ticket = ticket

    context = {
        'ticket': selected_ticket
    }

    return render(request, 'ticket_info.html', context)
