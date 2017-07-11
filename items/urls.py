from django.conf.urls import url

from items import views

urlpatterns = [
    url(r'^allergens/$', views.allergen_list, name='allergen_list'),
    url(r'^allergens/(?P<pk>\d+)/delete/$', views.allergen_delete, name='allergen_delete'),
    url(r'^items/', views.item_list, name='item_list'),
]