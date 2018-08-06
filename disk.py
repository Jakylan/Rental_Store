from datetime import datetime
import core


def read_file():
    with open('inventory.txt', 'r') as file:
        data = file.readlines()
    inventory = {}
    for item_info in data:
        item = item_info.split(',')
        item_name = item[0].strip()
        in_stock = int(item[1]).strip()
        price = int(item[2]).strip()
        inventory[item] = {
            'rental': item,
            'in-stock': in_stock,
            'price': price,
            'replacement': replacement
        }
    return inventory


def write_file(time, item, in_stock, price, replacement):
    text = '\n{}, {}, {}'.format(time, in_stock, price, replacement)

    with open('history.txt', 'a') as file:
        data = file.write(text)
