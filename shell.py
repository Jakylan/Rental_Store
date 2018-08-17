from datetime import datetime
import core
import disk


def customer_or_employee(inventory, revenue):
    print('\nHello Welcome to Base Camp Rentals!\n')
    while True:
        response = input('\nAre you a customer or a employee?\n').lower()
        if response == 'customer':
            print('\nGreat!')
            rent_or_return = input(
                'Are you renting or returning? ').lower().strip()
            if rent_or_return == 'renting':
                choose_console(inventory, revenue)
            elif rent_or_return == 'returning':
                return_item(inventory, revenue)
        elif response == 'employee':
            employee(inventory, revenue)
        elif response == 'no':
            print('\nHave a great day!\n')
            break
        elif response == 'quit':
            print('\nHave a great day!\n')
            break
        else:
            print('\nPlease provide an valid answer!\n')


def employee(inventory, revenue):
    while True:
        print('\nHi, employee!\n')
        print(
            "[1] See inventory\n[2] See History\n[3] See revenue\n[4] Quit\n")
        response = input("what would you like to do? ").strip()
        if response == '1':
            see_stock(inventory)
        elif response == '2':
            contents = disk.file_contents('history.txt')
            print(contents)
        elif response == '3':
            print('Revenue: {:.2f}'.format(revenue['total']))

        elif response == '4':
            exit()


def see_stock(inventory):
    for item in inventory:
        print("{} -- In Stock: {}".format(item, inventory[item]['in-stock']))


def print_inventory(inventory):
    for item in inventory:
        name = item
        in_stock = inventory[item]['in-stock']
        price = inventory[item]['price']
        replacement = inventory[item]['replacement']
        print('-----------------------------\n', name, '\nIn-Stock: ',
              in_stock, '\nPrice: ', price, '\nReplacement: ', replacement)
    print('-----------------------------')


def parse_inventory_item(string):
    if string.count(',') == 3:
        rental, in_stock, price, replacement = string.split(',')
        return [rental, int(in_stock), int(price), int(replacement)]
    else:
        return ['', 0, 0, 0]


def choose_console(inventory, revenue):
    for item in inventory:
        name = item
        in_stock = inventory[item]['in-stock']
        price = inventory[item]['price']
        replacement = inventory[item]['replacement']
        print('---------------------------------------- \n', name,
              '\nIn-Stock: ', in_stock, '\nPrice: ', price, '\nReplacement: ',
              replacement)
        print('----------------------------------------')
    while True:
        item = input('\nWhich console would you like?\n')
        if item in inventory:
            console = inventory[item]
            print('-----------------------------')
            print(f'You have chosen the {item}!')
            deposit = core.deposit(inventory, item)
            total = core.total(inventory, item, deposit)
            print('   Price:', inventory[item]['price'], 'Deposit:', deposit)
            print('Your Total With Taxes is {:.2f}'.format(total))
            print('Excellent choice!')
            # item_name = inventory[item]
            core.remove_from_stock(inventory, item)
            disk.write_file(item, inventory[item]['in-stock'], price,
                            replacement, 'Renting')
            disk.write_inventory(
                core.update_inventory(inventory), 'inventory.txt')
            core.update_inventory(inventory)
            core.add_to_revenue(revenue, inventory[item]['price'], deposit)
            string = core.revenue_string(revenue)
            disk.write_revenue(string, 'revenue.txt')
            # remove
            # save inventory
            # write history
            return item
        elif item == 'quit':
            break
        else:
            print(
                '\nSorry we do not have this in stock please choose another console!\n'
            )


def return_item(inventory, revenue):
    print_inventory(inventory)
    while True:
        item = input('What would you like to return? ')
        if item in inventory:
            core.add_to_stock(inventory, item)
            disk.write_file(item, inventory[item]['in-stock'],
                            inventory[item]['price'],
                            inventory[item]['replacement'], 'Returned')
            disk.write_inventory(
                core.update_inventory(inventory), 'inventory.txt')
            core.update_inventory(inventory)
            print('Item was successfully returned')
            deposit = core.deposit(inventory, item)
            print("Here is your deposit back\n${:.2f} ".format(deposit))
            core.subtract_revenue(revenue, deposit)
            string = core.revenue_string(revenue)
            disk.write_revenue(string, 'revenue.txt')
            break
        else:
            print('Cannot return that item here')


def main():
    file_info = disk.read_file('inventory.txt')
    revenue_info = disk.read_file('revenue.txt')
    revenue = core.revenue_dictionary(revenue_info)
    inventory = core.inventory_info(file_info)
    print(revenue_info)
    customer_or_employee(inventory, revenue)
    #item = choose_console(inventory)


if __name__ == '__main__':
    main()
