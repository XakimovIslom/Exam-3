from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductAPI.as_view(), name='product_list'),
    path('req/', views.RequestAPI.as_view(), name='request'),
    path('res/', views.ResultAPI.as_view(), name='response'),
]