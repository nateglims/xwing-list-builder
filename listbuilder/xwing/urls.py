from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.lists, name='root-page'),
    url(r'^lists/', views.lists, name='list-index'),
    url(r'^list/(?P<list_id>[0-9]+)/$', views.list, name='list'),
    url(r'^ships/', views.ships, name='ship-index'),
    url(r'^ship/(?P<ship_id>[0-9]+)/$', views.ship, name='ship'),
]
