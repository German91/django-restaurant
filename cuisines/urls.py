from django.conf.urls import url

from cuisines import views

urlpatterns = [
    url(r'^$', views.cuisine_list, name='cuisine_list'),
    url(r'^(?P<pk>\d+)/delete', views.cuisine_delete, name='cuisine_delete'),
]