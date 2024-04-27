from django.urls import path
from store import views

urlpatterns = [
    path("products/", views.CalculateTotalCost.as_view(), name="product_list"),
]