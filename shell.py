def parse_inventory_item(string):
    rental, in_stock, price = string.split(',')
    return [rental, int(in_stock), int(price)]


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
        print('   Rental', console['Rental'])
        print('   In-Stock', console['In-Stock'])
        print('   Price', console['Price'])
    while True:
        item = input('\nWhich console would you like?\n')
        if item in inventory:
            print('Excellent choice!')
            break
        elif item == 'quit':
            break
        else:
            print(
                '\nSorry we do not have this in stock please choose anther console!\n'
            )


def main():
    inventory = load_inventory()
    print('\nHello welcome to Base Camp Rentals!\n')
    response = input('\nAre you a customer or a employee?\n')
    while True:
        if response == 'customer':
            print('\nGreat!')
            response = input('\nWould you like to rent a console?\n')
            if response == 'yes':
                choose_console(inventory)
        elif response == 'employee':
            print('\nHi, employee!\n')
            response = input('\nWould you like to view the inventory?\n')
            if response == 'yes':
                print(inventory)
            elif response == 'no':
                print('\nHave a great day!\n')
                break
        elif response == 'quit':
            print('\nHave a great day!\n')
            break


if __name__ == '__main__':
    main()
