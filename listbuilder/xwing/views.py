from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import List, Ship


def list(request, list_id):
    l = get_object_or_404(List, pk=list_id)
    return render(request, 'xwing/list.html', {'list': l})


def ship(request, ship_id):
    s = get_object_or_404(Ship, pk=ship_id)
    return render(request, 'xwing/ship.html', {'ship': s})


def ships(request):
    s = Ship.objects.all()
    return render(request, 'xwing/ships.html', {'ships': s})


def lists(request):
    l = List.objects.all()
    return render(request, 'xwing/lists.html', {'lists': l})
