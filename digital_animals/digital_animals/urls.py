from django.conf.urls import include, url
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)
from django.contrib import admin

handler400 = 'website.views.handler400'
handler403 = 'website.views.handler403'
handler404 = 'website.views.handler404'
handler500 = 'website.views.handler500'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('website.urls')),
]
