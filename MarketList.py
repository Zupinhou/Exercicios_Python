Market_list = []

def list_validation():
    if Market_list == []:
        return False
    else:
        return True

def add_product():
    buyer = input('Enter product to buy: ')
    while buyer != '':
        if buyer.strip():
            if buyer in Market_list:
                print(f'The item "{buyer}" exists in list')
            else:
                Market_list.append(buyer)
                print(f'{buyer} added to list')
        buyer = input('Enter product to buy: ')

def remove_product():
    print('Do you want to remove any product from the list?')
    buyer = input('Yes [Y] or No [N]: ').upper()
    while buyer != 'Y' and buyer != 'N':
        print('Invalid option')
        buyer = input('Yes [Y] or No [N]: ').upper()
    if buyer == 'Y':
        while buyer != '':
            if Market_list == []:
                print('List is empty')
                break
            buyer = input('Enter product to remove (or press enter to cancel): ')
            if buyer == '':
                break
            elif buyer in Market_list:
                Market_list.remove(buyer)
                print(f'{buyer} removed from list')
                print(Market_list)
            else:
                print(f'{buyer} not in list')
                print(Market_list)
    else:
        print('Thanks for list')

def show_list():
    print('Do you want to see the list?')
    buyer = input('Yes [Y] or No [N]: ').upper()
    while buyer != 'Y' and buyer != 'N':
        print('Invalid option')
        buyer = input('Yes [Y] or No [N]: ').upper()
    if buyer == 'Y':
        print(Market_list)
    else:
        print('Thanks for list')

def main():
    print('Welcome to the market list')
    add_product()
    if list_validation() is not False:
        remove_product()
    if list_validation() is not False: 
        show_list()

if __name__ == "__main__":
    main()
