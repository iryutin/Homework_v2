from src.classes import Category


def test_product(product_samsung):
    """Тест класса продукт"""
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5


def test_category(product_samsung, product_iphone, categori_smartfone):
    """Тест класса категории"""
    assert categori_smartfone.name == "Смартфоны"
    assert (
        categori_smartfone.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert categori_smartfone.products == [product_samsung, product_iphone]
    assert Category.product_count == 3
    assert Category.category_count == 2
