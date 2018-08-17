def remove_from_stock(inventory, item_name):
    inventory[item_name]['in-stock'] -= 1
    return inventory


def add_to_stock(inventory, item):
    inventory[item]['in-stock'] += 1
    return inventory


def deposit(inventory, item):
    total = inventory[item]['replacement'] * .10
    return round(total, 2)


def total(inventory, item, deposit):
    total = (inventory[item]['price'] * 1.07) + deposit
    return round(total, 2)


def inventory_info(data):
    inventory = {}
    for item_info in data:
        item = item_info.split(',')
        item_name = item[0]
        in_stock = int(item[1])
        price = int(item[2])
        replacement = int(item[3])
        inventory[item_name] = {
            'in-stock': in_stock,
            'price': price,
            'replacement': replacement
        }
    return inventory


def revenue_dictionary(data):
    revenue = {}
    for info in data:
        items = info.split(',')
        key = items[0]
        value = float(items[1])
        revenue[key] = value
    return revenue


def update_inventory(inventory):
    header = 'rental, in-stock, price, replacement'
    for item in inventory:
        header += f"\n{item}, {inventory[item]['in-stock']}, {inventory[item]['price']}, {inventory[item]['replacement']}"
    return header


def add_to_revenue(revenue, item, deposit):
    for key in revenue:
        revenue[key] += item + deposit
    return revenue


def subtract_revenue(revenue, deposit):
    for key in revenue:
        revenue[key] -= deposit
    return revenue


def revenue_string(revenue):
    text = 'total, value\n'
    for key in revenue:
        text += '{}, {}'.format(key, revenue[key])
        return text
