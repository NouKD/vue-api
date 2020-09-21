from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exo', views.exo, name='exo'),
    path('exo2', views.exo2, name='exo2'),
    path('postdata', views.postdata, name='postdata'),
    path('pdata', views.pdata, name='pdata'),
    path('podata', views.podata, name='podata'),
]