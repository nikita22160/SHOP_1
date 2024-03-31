class Category:
    """
    Класс описывающий категорию продуктов, имеющий атрибуты имени, описания и списка продукции,
    а также счетчик задействованных уникальных продуктов в списке и категорий товаров.
    """
    name: str
    description: str
    products: list
    all_quantity_category = 0
    all_quantity_unique_product = 0

    def __init__(self, name: str, description: str, products: list):
        """
        Метод для инициализации класса Category
        """
        self.name = name
        self.description = description
        self.products = products

        Category.all_quantity_category += 1     # Подсчитывает категории товаров
        Category.all_quantity_unique_product += len(set(self.products))   # Подсчитывает уникальные продукты

        self.categories_count = Category.all_quantity_category
        self.product_count = Category.all_quantity_unique_product