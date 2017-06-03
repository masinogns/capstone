from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from mysite.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),

    url(r'^jejudaum/', include('jejudaum.urls', namespace='jejudaum')),
    url(r'^menza/', include('menza.urls', namespace='menza')),

    url(r'^$', IndexView.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
