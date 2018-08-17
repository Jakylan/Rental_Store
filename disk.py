from datetime import datetime
import core


def read_file(file):
    with open(file, 'r') as file:
        file.readline()
        data = file.readlines()
    return data


def file_contents(file):
    with open(file) as file:
        contents = file.read()
    return contents


def write_file(item, in_stock, price, replacement, action):
    text = '\n{}, {}, {}, {}, {}'.format(datetime.now(), in_stock, price,
                                         replacement, action)

    with open('history.txt', 'a') as file:
        data = file.write(text)


def write_revenue(string, file):
    with open(file, 'w') as file:
        file.write(string)


def write_inventory(inventory, file):
    with open(file, 'w') as file:
        file.write(inventory)
