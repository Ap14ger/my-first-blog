from django.urls import path
from . import views


urlpatterns = [
    # trae de views el metodo post_list
    path('', views.post_list, name='post_list'),
]
