from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('<str:shortcode>/', views.redirect_url, name='redirect_url'),
]