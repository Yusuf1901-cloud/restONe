from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.SearchListVIew.as_view(), name='search'),
]