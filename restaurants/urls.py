from django.conf.urls import url

from restaurants import views

urlpatterns = [
  url(r'^$', views.restaurant_list, name='restaurant_list'),
  url(r'^add/$', views.restaurant_add, name='restaurant_add'),
  url(r'^(?P<slug>[\w-]+)/$', views.restaurant_view, name='restaurant_view'),
  url(r'(?P<pk>\d+)/archive/$', views.restaurant_archive, name='restaurant_archive'),
]