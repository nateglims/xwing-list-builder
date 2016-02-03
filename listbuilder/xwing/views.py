from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import List, Ship


def list(request, list_id):
    l = get_object_or_404(List, pk=list_id)
    return HttpResponse("You're looking for list %s with points %s and ships %s" %
                         (l.name, l.max_points, [s.name for s in l.ships.all()],) )


def ship(request, ship_id):
    s = get_object_or_404(Ship, pk=ship_id)
    return HttpResponse("You're looking for ship {}".format(s.name))


def ships(request):
    ships = Ship.objects.all()
    return HttpResponse("This is all the ships...\n%s" % '\n'.join([s.name for s in ships]))


def lists(request):
    lists = List.objects.all()
    return HttpResponse("This is all the lists!\n%s" % '\n'.join([l.name for l in lists]))
