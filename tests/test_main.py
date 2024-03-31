import pytest

from classes.category import Category
from classes.product import Product

@pytest.fixture
def test_correct_init_category():
    return Category("Смартфоны", "Cмартфоны, как средство не только коммуникации, "
                                 "но и получения дополнительных функций для удобства жизни", [1, 2, 3, 4])


def test_init(test_correct_init_category):
    assert test_correct_init_category.name == 'Смартфоны'
    assert test_correct_init_category.description == ('Cмартфоны, как средство не только коммуникации, '
                                                      'но и получения дополнительных функций для удобства жизни')
    assert test_correct_init_category.products == [1, 2, 3, 4]


@pytest.fixture
def test_correct_init_product():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_init_for_second_class(test_correct_init_product):
    assert test_correct_init_product.name == 'Samsung Galaxy C23 Ultra'
    assert test_correct_init_product.description == '256GB, Серый цвет, 200MP камера'
    assert test_correct_init_product.price == 180000.0
    assert test_correct_init_product.quantity == 5


@pytest.fixture
def test_correct_init_numb():
    return Category("Смартфоны", "Cмартфоны, как средство не только коммуникации, "
                                 "но и получения дополнительных функций для удобства жизни", [1, 2, 3, 4])


def test_summ_numb(test_correct_init_numb):
    assert test_correct_init_numb.categories_count == 2
    assert test_correct_init_numb.product_count == 8