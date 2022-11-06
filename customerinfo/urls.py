from django.urls import path
from . import views

urlpatterns = [
    path('', views.about2, name=''),
    path('', views.about, name=''),
]