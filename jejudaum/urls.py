from django.conf.urls import url

from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^list$', RoomList.as_view(), name='room_list'),
    url(r'^detail/(?P<pk>\d+)$', RoomDetail.as_view(), name='room_detail'),
    url(r'^new$', login_required(RoomCreate.as_view()), name='room_new'),
    url(r'^edit/(?P<pk>\d+)$', login_required(RoomUpdate.as_view()), name='room_edit'),
    url(r'^delete/(?P<pk>\d+)$', login_required(RoomDelete.as_view()), name='room_delete'),
    url(r'^change/$',login_required(RoomChangeList.as_view()), name="room_change"),
]
