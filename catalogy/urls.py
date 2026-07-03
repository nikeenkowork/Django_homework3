from django.urls import path, include
from .views import (
    HomeView,
    ProductListView,
    ProductDetailView,
    ContactsView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),

    # CRUD PRODUCTS
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),

    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),

    path("contacts/", ContactsView.as_view(), name="contacts"),

    path("blog/", include("blog.urls")),
]
