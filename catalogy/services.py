from .models import Product
from django.core.cache import cache


def get_products_by_category(category):
    """
    Возвращает список продуктов указанной категории
    """
    return Product.objects.filter(category=category)


def get_products():
    cache_key = "all_products"

    products = cache.get(cache_key)

    if products is None:
        products = list(Product.objects.all())
        cache.set(cache_key, products, 60 * 15)  # 15 минут

    return products
