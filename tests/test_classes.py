import pytest

from src.classes import Category, LawnGrass, Product, Smartphone


def test_product(product_samsung, product_iphone, capsys):
    """Тест класса продукт"""
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    print(product_samsung)
    captured = capsys.readouterr()
    assert captured.out == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
    assert product_samsung + product_iphone == 2580000.0
    product_samsung.price = 1
    assert product_samsung.price == 1.0
    assert product_samsung.quantity == 5
    with pytest.raises(AttributeError):
        print(product_samsung.__price)


def test_category(product_samsung, product_iphone, categori_smartfone, capsys):
    """Тест класса категории"""
    assert categori_smartfone.name == "Смартфоны"
    assert (
        categori_smartfone.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert Category.product_count == 3
    assert Category.category_count == 2
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    categori_smartfone.add_product(product4)
    print(categori_smartfone.products)
    captured = capsys.readouterr()
    assert (
        captured.out
        == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. Остаток: 8 шт.\n55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n\n'
    )
    print(categori_smartfone)
    captured = capsys.readouterr()
    assert captured.out == "Смартфоны, количество продуктов: 20 шт.\n"


def test_smartfone_and_trava_summ(smartphone1, grass1):
    with pytest.raises(TypeError):
        invalid_sum = smartphone1 + grass1


def test_not_a_product(smartphone1):
    category_smartphones = Category(
        "Смартфоны", "Высокотехнологичные смартфоны", [smartphone1]
    )
    with pytest.raises(TypeError):
        category_smartphones.add_product("Not a product")
