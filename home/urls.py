from django.urls import path
from home import views

urlpatterns = [
    path('', views.inicio),
    path('profesores/', views.profesores, name='profesor'),
]
