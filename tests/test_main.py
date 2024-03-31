import pytest

from classes.category import Category
from classes.product import Product


@pytest.fixture()
def product_iphone():
    return Product('Iphone 15', '512Gb, Gray space', 210000.0, 8)


@pytest.fixture()
def product_intel():
    return Product('i514500', 'L1 16Mb, L2 32Mb, L3 64Mb', 30000.0, 15)


@pytest.fixture()
def category_smartphones():
    return Category('Smartphones', 'Smarter than humans',
                    [Product('Iphone 15', '512Gb, Gray space', 210000.0, 8),
                     Product('Galaxy 10', '256GB, Green', 150000.0, 5)])


@pytest.fixture()
def adding_products():
    data_for_product = {
        'name': 'Iphone 15 Pro',
        'description': '512Gb Red',
        'price': 250000.0,
        'quantity': 5
    }
    return Product.creating_product(data_for_product)


def test_product_init(product_iphone):
    assert product_iphone.name == 'Iphone 15'
    assert product_iphone.description == '512Gb, Gray space'
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8


def test_product_init_2(product_intel):
    assert product_intel.name == 'i514500'
    assert product_intel.description == 'L1 16Mb, L2 32Mb, L3 64Mb'
    assert product_intel.price == 30000.0
    assert product_intel.quantity == 15


def test_category_init(category_smartphones):
    assert category_smartphones.name == 'Smartphones'
    assert category_smartphones.description == 'Smarter than humans'
    assert category_smartphones.all_quantity_category == 1
    assert category_smartphones.all_quantity_unique_product == 2
    assert (category_smartphones.getting_list_of_product ==
            'Iphone 15, 210000.0 руб. Остаток: 8 шт.Galaxy 10, 150000.0 руб. Остаток: 5 шт.')
