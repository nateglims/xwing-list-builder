from django.conf.urls import url

from .views import ListDetailView, ListListView, ShipDetailView, ShipListView

urlpatterns = [
    url(r'^$', ListListView.as_view(), name='root-page'),
    url(r'^lists/', ListListView.as_view(), name='list-index'),
    url(r'^list/(?P<list_id>[0-9]+)/$', ListDetailView.as_view(), name='list),
    url(r'^ships/', ShipListView.as_view(), name='ship-index'),
    url(r'^ship/(?P<ship_id>[0-9]+)/$', ShipDetailView.as_view(), name='ship'),
]
