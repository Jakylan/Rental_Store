from datetime import datetime
from core import *


def customer_or_employee():
    inventory = load_inventory()
    print('\nHello welcome to Base Camp Rentals!\n')
    while True:
        response = input('\nAre you a customer or a employee?\n')
        if response == 'customer':
            print('\nGreat!')
            response = input('\nWould you like to rent a console?\n')
            if response == 'yes':
                print('----------------------------------------')
                choose_console(inventory)
                break
        elif response == 'employee':
            print('\nHi, employee!\n')
            response = input('\nWould you like to view the inventory?\n')
            if response == 'yes':
                print(inventory)
                break
            elif response == 'no':
                print('\nHave a great day!\n')
                break
        elif response == 'quit':
            print('\nHave a great day!\n')
            break
        else:
            print('\nPlease provide an valid answer!\n')


def parse_inventory_item(string):
    rental, in_stock, price = string.split(',')
    return [rental, int(in_stock), int(price)]


def inventory():
    inventory = [{
        'rental': 'Xbox One X',
        'in-stock': 30,
        'price': 175
    }, {
        'rental': 'PlayStation 4 Pro 1TB',
        'in-stock': 25,
        'price': 150,
    }, {
        'rental': 'Super NES Classic',
        'in-stock': 20,
        'price': 75
    }]


def load_inventory():
    with open('inventory.txt', 'r') as file:
        string = file.read()
    inventory = {}
    lines = string.split('\n')[1:]
    for line in lines:
        if line:
            d = parse_inventory_item(line)
            inventory[d[0]] = {
                'Rental': d[0],
                'In-Stock': d[1],
                'Price': d[2],
            }

    return inventory


def print_inventory(inventory):
    for item in inventory:
        print(item)


def choose_console(inventory):
    for item in inventory:
        console = inventory[item]
        print(item)
        print('   Rental:', console['Rental'])
        print('   In-Stock:', console['In-Stock'])
        print('   Price:', console['Price'])
        print('----------------------------------------')
    while True:
        item = input('\nWhich console would you like?\n')
        if item in inventory:
            if item == 'Xbox One X':
                print('----------------------------------------')
                print('You have chosen the Xbox One X!')
                print('   Price:', console['Price'])
                print('Excellent choice!')
                break
            if item == 'PlayStation 4 Pro 1TB':
                print('----------------------------------------')
                print('You have chosen the PlayStation 4 Pro 1TB')
                print('   Price:', console['Price'])
                print('Excellent choice!')
                break
            if item == 'Super NES Classic':
                print('----------------------------------------')
                print('You have chosen the Super NES Classic!')
                print('   Price:', console['Price'])
                print('Excellent choice!')
                break
        elif item == 'quit':
            break
        else:
            print(
                '\nSorry we do not have this in stock please choose another console!\n'
            )


def write_to_history(item, price, time):
    price = get_game_price()
    item = choose_console()
    time = datetime.now()
    text = '\n{}, {}, {}'.format(item, price, time)
    with open('history.txt', 'a') as file:
        file.write(text)


def main():
    customer_or_employee()
    inventory = load_inventory()
    item = choose_console
    price = get_game_price()
    write_to_history(item, price, time)
    inventory()


if __name__ == '__main__':
    main()
