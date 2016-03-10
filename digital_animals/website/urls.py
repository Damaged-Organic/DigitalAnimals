from django.conf.urls import url

from . import views

app_name = 'website'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^order$', views.order, name='order'),
    url(r'^order/send$', views.order_send, name='order_send'),
]
