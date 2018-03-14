from django.conf.urls import url
from django.contrib.auth import views

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
]