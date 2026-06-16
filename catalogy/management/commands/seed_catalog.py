from django.core.management.base import BaseCommand

from catalogy.models import Category, Product


class Command(BaseCommand):
    help = "Удаляет старые данные и создаёт тестовые продукты"

    def handle(self, *args, **options):
        # 🔥 удаляем всё
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write(self.style.WARNING("Старые данные удалены"))

        # 📦 категории
        electronics = Category.objects.create(
            name="Электроника", description="Гаджеты и устройства"
        )

        books = Category.objects.create(name="Книги", description="Учебная литература")

        clothes = Category.objects.create(name="Одежда", description="Мода и стиль")

        # 🛒 продукты
        Product.objects.create(
            name="iPhone 15",
            description="Смартфон Apple",
            category=electronics,
            purchase_price=999.99,
        )

        Product.objects.create(
            name="MacBook Air",
            description="Ноутбук Apple",
            category=electronics,
            purchase_price=1299.99,
        )

        Product.objects.create(
            name="Django Book",
            description="Учебник по Django",
            category=books,
            purchase_price=29.99,
        )

        Product.objects.create(
            name="Nike Hoodie",
            description="Толстовка",
            category=clothes,
            purchase_price=59.99,
        )

        self.stdout.write(self.style.SUCCESS("Тестовые данные успешно созданы"))
