from django.conf.urls import url

from cuisines import views

urlpatterns = [
    url(r'^$', views.cuisine_list, name='cuisine_list'),
]