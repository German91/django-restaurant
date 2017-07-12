"""restaurantsapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^$', views.login, name='login', kwargs={'redirect_authenticated_user': True}),
    url(r'^restaurants/', include('restaurants.urls')),
    url(r'^cuisines/', include('cuisines.urls')),
    url(r'^sections/', include('sections.urls')),
    url(r'^categories/', include('categories.urls')),
    url(r'^items/', include('items.urls')),
]
