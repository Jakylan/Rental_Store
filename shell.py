from datetime import datetime
import core
import disk


def customer_or_employee(inventory):
    print('\nHello welcome to Base Camp Rentals!\n')
    while True:
        response = input('\nAre you a customer or a employee?\n').lower()
        if response == 'customer':
            print('\nGreat!')
            response = input('\nWould you like to rent a console?\n').lower()
            if response == 'yes':
                print('----------------------------------------')
                return True
        elif response == 'employee':
            print('\nHi, employee!\n')
            response = input(
                '\nWould you like to view the inventory?\n').lower()
            if response == 'yes':
                print(inventory)
                exit()
        elif response == 'no':
            print('\nHave a great day!\n')
            break
        elif response == 'quit':
            print('\nHave a great day!\n')
            break
        else:
            print('\nPlease provide an valid answer!\n')


def print_inventory(inventory):
    for item in inventory:
        print(item)


def parse_inventory_item(string):
    if string.count(',') == 3:
        rental, in_stock, price, replacement = string.split(',')
        return [rental, int(in_stock), int(price), int(replacement)]
    else:
        return ['', 0, 0, 0]


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
                'Replacement': d[3]
            }

    return inventory


def write_inventory(inventory):
    time = datetime.now()
    text = '\n{}, {}, {}'.format(time, item, price)
    with open('history.txt', 'r') as file:
        string = file.readlines(text)


def choose_console(inventory):
    for item in inventory:
        console = inventory[item]
        print(item)
        print('   Rental:', console['Rental'])
        print('   In-Stock:', console['In-Stock'])
        print('   Price:', console['Price'])
        print('   Replacement:', console['Price'] * .10)
        print('----------------------------------------')
    while True:
        item = input('\nWhich console would you like?\n')
        if item.lower() in 'Xbox One X'.lower():
            print('----------------------------------------')
            print('You have chosen the Xbox One X!')
            print('   Price:', console['Price'])
            print('Excellent choice!')
            return 'Xbox One X'
        elif item.lower() in 'PlayStation 4 Pro 1TB'.lower():
            print('----------------------------------------')
            print('You have chosen the PlayStation 4 Pro 1TB')
            print('   Price:', console['Price'])
            print('Excellent choice!')
            return 'Playstation 4 Pro 1TB'
        elif item.lower() in 'Super NES Classic'.lower():
            print('----------------------------------------')
            print('You have chosen the Super NES Classic!')
            print('   Price:', console['Price'])
            print('Excellent choice!')
            return 'Super NES Classic'
        elif item == 'quit':
            break
        else:
            print(
                '\nSorry we do not have this in stock please choose another console!\n'
            )


def main():
    inventory = load_inventory()
    customer = customer_or_employee(inventory)
    if customer:
        item = choose_console(inventory)
        time = datetime.now()
        console = inventory[item]
        in_stock = console['In-Stock']
        price = console['Price']
        replacement = console['Price'] * .10
        disk.write_file(time, item, in_stock, price, replacement)


if __name__ == '__main__':
    main()
