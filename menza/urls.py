from django.conf.urls import url

from .views import *

urlpatterns = [
    # url(r'^$', IndexView.as_view(), name='index'),
    # url(r'^$', IndexView.as_view(), name='index'),
    url(r'^$', ContentList.as_view(), name='list'),
    url(r'^upload$', upload, name ='upload'),
    url(r'^photo/(?P<pk>\d+)/$', ContentDetail.as_view(), name='detail'),
]
