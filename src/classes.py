class Product:
    """Класс продукты с именем описанием ценой и колличеством на складе"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(product_data['name'], product_data['description'], product_data['price'], product_data['quantity'])

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price (self, new_price: float):
        self.__price = float(new_price)


class Category:
    """Класс категории с именем описанием списком продуктов,
    так же отдельный глобальный подсчёт категорий и продуктов"""

    name: str
    description: str
    __products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(products)
        Category.category_count += 1

    def add_product(self, products):
        self.__products.append(products)
        Category.product_count += 1

    @property
    def products(self):
        product_sring = ''
        for product in self.__products:
            product_sring += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return product_sring
