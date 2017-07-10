from django.conf.urls import url

from restaurants import views

urlpatterns = [
  url(r'^restaurants/$', views.restaurant_list, name='restaurant_list'),
]