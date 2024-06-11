from django.urls import path
from home import views

urlpatterns = [
    path('', views.inicio),
    path('template/', views.template),
]
