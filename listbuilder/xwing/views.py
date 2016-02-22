from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from .models import List, Ship


class ListDetailView(DetailView):
    template_name = 'xwing/list.html'
    model = List


class ShipDetailView(DetailView):
    template_name = 'xwing/ship.html'
    model = Ship


class ShipListView(ListView):
    template_name = 'xwing/ships.html'
    model = Ship


class ListListView(ListView):
    template_name = 'xwing/lists.html'
    model = List