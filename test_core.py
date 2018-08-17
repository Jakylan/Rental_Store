import core


def test_remove_from_stock():
    inventory = {
        'Xbox One X': {
            'in-stock': 21,
            'price': 175,
            'replacement': 300
        },
    }
    assert core.remove_from_stock(inventory, 'Xbox One X') == {
        'Xbox One X': {
            'in-stock': 20,
            'price': 175,
            'replacement': 300
        },
    }


def test_add_to_stock():
    inventory = {
        'Xbox One X': {
            'in-stock': 21,
            'price': 175,
            'replacement': 300
        },
    }
    assert core.add_to_stock(inventory, 'Xbox One X') == {
        'Xbox One X': {
            'in-stock': 22,
            'price': 175,
            'replacement': 300
        },
    }


def test_deposit():
    inventory = {
        'Xbox One X': {
            'in-stock': 21,
            'price': 1,
            'replacement': 300
        },
    }
    assert core.deposit(inventory, 'Xbox One X') == 30.00


def test_total():
    inventory = {
        'Xbox One X': {
            'in-stock': 21,
            'price': 1,
            'replacement': 300
        },
    }
    assert core.total(inventory, 'Xbox One X', 1) == 2.07


def test_inventory_info():
    data = ['Xbox One X, 21, 175, 300']
    assert core.inventory_info(data) == {
        'Xbox One X': {
            'in-stock': 21,
            'price': 175,
            'replacement': 300
        },
    }


def test_revenue_dictionary():
    data = ['total, 380.0']
    assert core.revenue_dictionary(data) == {'total': 380.0}


def test_update_inventory():
    inventory = {
        'Xbox One X': {
            'in-stock': 21,
            'price': 175,
            'replacement': 300
        },
    }
    assert core.update_inventory(
        inventory
    ) == 'rental, in-stock, price, replacement\nXbox One X, 21, 175, 300'


def test_add_to_revenue():
    revenue = {'total': 10}
    item = 20
    deposit = 10
    assert core.add_to_revenue(revenue, item, deposit) == {'total': 40}


def test_substract_revenue():
    revenue = {'total': 25}
    deposit = 15
    assert core.subtract_revenue(revenue, deposit) == {'total': 10}


def test_revenue_string():
    revenue = {'total': 30}
    assert core.revenue_string(revenue) == 'total, value\ntotal, 30'
