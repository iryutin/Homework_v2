import pytest

from src.classes import Category, Product


@pytest.fixture
def product_samsung():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def product_iphone():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def categori_smartfone(product_iphone, product_samsung):
    category2 = Category(
        "заглушка", "заглушка", ["заглушка"]
    )  # категория заглушка для теста подщёта количества категорий
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product_samsung, product_iphone],
    )
