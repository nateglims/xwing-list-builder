from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.lists, name='List Index'),
    url(r'^lists/', views.lists, name='List Index'),
    url(r'^list/(?P<list_id>[0-9]+)/$', views.list, name=''),
    url(r'^ships/', views.ships, name='Ship Index'),
    url(r'^ship/(?P<ship_id>[0-9]+)/$', views.ship, name=''),
]
