def parse_inventory_item(string):
    rental, in_stock, = string.split(',')
    return [rental, int(in_stock)]


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
    print('\Hello welcome to Base Camp Rentals!\n')
    response = input('\nAre you a customer or a employee?\n')

    if response == 'customer':
        print('\nGreat!')
        print('''
        1 - Nintendo Switch
        2 - Xbox One X
        3 - PlayStation 4 Pro 1TB
        4 - Nintendo Wii U
        5 - Xbox 360 E Console
        6 - PlayStation 3
        7 - Super NES Classic
        8 - Nintendo 3DS XL
        ''')
        response = input('\nWould you like to rent a console?\n')
        if response == 'yes':
            choose_console(inventory)
            if response == '1':
                print('\nYou have chosen the Nintendo Switch.\n')
            elif response == '2':
                print('\nYou have chosen the Xbox One X.\n')
            elif response == '3':
                print('\nYou have chosen the PlayStaion 4 Pro 1TB.\n')
            elif response == '4':
                print('\nYou have chosen the Nintendo Wii U.\n')
            elif response == '5':
                print('\nYou have chosen the Xbox 360 E Console.\n')
            elif response == '6':
                print('\nYou have chosen the PlayStation 3.\n')
            elif response == '7':
                print('\nYou have chosen the Super NES Classic.\n')
            elif response == '8':
                print('\nYou have chosen the Nintendo 3DS XL.\n')

    elif response == 'employee':
        print('\nHi, employee!\n')
        response = input('\nWould you like to view the inventory?\n')
        if response == 'yes':
            print(inventory)
        elif response == 'no':
            print('\nHave a great day!\n')
            exit()
    elif response == 'quit':
        print('\nHave a great day!\n')
        exit()


if __name__ == '__main__':
    main()
