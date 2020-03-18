import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {"Pen": {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products


@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


def test_CanCalculateTotalImpurePrice(invoice, products):
    testTotalImpurePrice = invoice.totalImpurePrice(products)
    assert testTotalImpurePrice == 75


def test_CanCalculateTotalDiscount(invoice, products):
    testTotalDiscount = invoice.totalDiscount(products)
    assert testTotalDiscount == 5.62


def test_CanCalculateTotalPurePrice(invoice, products):
    testTotalPurePrice = invoice.totalPurePrice(products)
    assert testTotalPurePrice == 69.38

def test_Canadd(invoice):
    tmp = {'qnt': 1, 'unit_price': 1, 'discount': 10}
    output = invoice.addProduct(1, 1, 10)
    assert tmp == output
