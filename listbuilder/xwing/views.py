from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from .models import List, Ship


class ListDetailView(DetailView):
    template_name = 'xwing/list.html'
    model = List

    def get(self, request, *args, **kwargs):
        l = get_object_or_404(List, pk=kwargs['list_id'])
        return render(request, self.template_name, {'list': l})


class ShipDetailView(DetailView):
    template_name = 'xwing/ship.html'
    model = Ship

    def get(self, request, *args, **kwargs):
        s = get_object_or_404(Ship, pk=kwargs['ship_id'])
        return render(request, self.template_name, {'ship': s})


class ShipListView(ListView):
    template_name = 'xwing/ships.html'
    model = Ship


class ListListView(ListView):
    template_name = 'xwing/lists.html'
    model = List