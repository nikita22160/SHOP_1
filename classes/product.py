class Product:
    """
    Класс для продуктов, который имеет атрибуты имени, описания, цены и количества
    """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Метод для инициализации атрибутов класса Product
        """
        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity = quantity
