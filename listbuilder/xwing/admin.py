from django.contrib import admin

from .models import List, Ship, ListShipInclusion

admin.site.register(List)
admin.site.register(Ship)
admin.site.register(ListShipInclusion)
