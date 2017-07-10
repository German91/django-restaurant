from django.conf.urls import url

from restaurants import views

urlpatterns = [
  url(r'^$', views.restaurant_list, name='restaurant_list'),
  url(r'^add/$', views.restaurant_add, name='restaurant_add'),
]