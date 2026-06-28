from django.urls import path
from .views import (
    HomeView,
    ProductListView,
    ProductDetailView,
    ContactsView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("blog/", include("blog.urls")
]
