from django.conf.urls import url

from sections import views

urlpatterns = [
    url(r'^add/$', views.section_add, name='section_add'),
    url(r'^(?P<pk>\d+)/delete/$', views.section_delete, name='section_delete'),
    url(r'^(?P<slug>[\w-]+)/$', views.section_view, name='section_view'),
]