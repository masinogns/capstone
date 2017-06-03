from django.conf.urls import url

from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # url(r'^$', IndexView.as_view(), name='index'),

    url(r'^$', ContentList.as_view(), name='list'),
    url(r'^upload$', upload, name ='upload'),
    # url(r'^upload$', login_required(ContentCreate), name ='upload'),
    url(r'^mylist/', login_required(MyListView.as_view()), name ='my_list'),
    url(r'^photo/(?P<pk>\d+)/$', ContentDetail.as_view(), name='detail'),
    # url(r'^edit/(?P<pk>\d+)$', login_required(ContentUpdate.as_view()), name='update'),
    url(r'^edit/(?P<pk>\d+)$', edit, name='update'),
    url(r'^delete/(?P<pk>\d+)$', login_required(ContentDelete.as_view()), name='delete'),
]
