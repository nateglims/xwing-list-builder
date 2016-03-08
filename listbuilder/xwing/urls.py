from django.conf.urls import url

from .views import ListDetailView, ListListView, ShipDetailView, ShipListView, ListCreateView

urlpatterns = [
    url(r'^$', ListListView.as_view(), name='root-page'),
    url(r'^lists/', ListListView.as_view(), name='list-index'),
    url(r'^list/(?P<pk>[0-9]+)/$', ListDetailView.as_view(), name='list'),
    url(r'^listform/',ListCreateView.as_view(), name='list-create'),
    url(r'^ships/', ShipListView.as_view(), name='ship-index'),
    url(r'^ship/(?P<pk>[0-9]+)/$', ShipDetailView.as_view(), name='ship'),
]
