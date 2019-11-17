from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views


urlpatterns = [
    url(r'^/carts/$', views.CartsView.as_view()),
]