from django.conf.urls import url

from categories import views

urlpatterns = [
    url(r'^add/', views.category_add, name='category_add'),
]