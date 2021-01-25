from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:trackingNumber>/', views.detail, name='detail'),
]