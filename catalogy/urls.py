from django.urls import path, include
from django.views.decorators.cache import cache_page

from .views import (
    HomeView,
    ProductListView,
    ProductDetailView,
    ContactsView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    unpublish_product,
    ProductsByCategoryView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    # CRUD PRODUCTS
    path("products/", ProductListView.as_view(), name="product_list"),
    path(
        "products/<int:pk>/",
        cache_page(60 * 15)(ProductDetailView.as_view()),
        name="product_detail",
    ),
    path(
        "products/category/<str:category>/",
        ProductsByCategoryView.as_view(),
        name="products_by_category",
    ),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    path(
        "products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    # Снять товар с публикации
    path("products/<int:pk>/unpublish/", unpublish_product, name="unpublish_product"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("blog/", include("blog.urls")),
]
