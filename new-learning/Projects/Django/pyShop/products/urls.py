from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('newProduct', views.newProduct),
    path('wellness', views.newStore)
]
