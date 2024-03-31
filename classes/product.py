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
        self.__price = float(price)
        self.quantity = quantity

    @classmethod
    def creating_product(cls, product_data: dict):
        return cls(**product_data)


    @property
    def price(self):
        """
        Метод-геттер для атрибута цены
        """
        return self.__price

    @price.setter
    def price(self, new_price):
        """
        Метод setter для атрибута цены.
        Принимает новое значение, если цена <= 0 print('Цена введена некорректно'), при этом цена не устанавливается.\
        В случае если цена товара понижается, добавьте логику подтверждения пользователем вручную
        через ввод y(значит yes) или n (значит no) для согласия понизить цену или для отмены действия соответственно.
        """
        if new_price <= 0:
            print('Цена введена некорректно')
        elif new_price > self.__price:
            self.__price = new_price
            print('Цена повышена')
        elif new_price < self.__price:
            user_answer = input('Подтвердите понижение цены: y/n ')
            if user_answer == 'y':
                self.__price = new_price
                print('Цена понижена')
