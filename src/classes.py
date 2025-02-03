class Product:
    """Класс продукты с именем описанием ценой и колличеством на складе"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс категории с именем описанием списком продуктов,
    так же отдельный глобальный подсчёт категорий и продуктов"""

    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.product_count += len(products)
        Category.category_count += 1
