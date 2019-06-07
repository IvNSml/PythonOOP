from random import randrange

from CoffeeShop import CoffeeShop
from CustomerDef import Customer
from God import God
from Manager import Manager


def main():
    Zeus = God()
    customers = []
    coffeeshops = []
    for i in range(5):
        customers.append(Customer(Zeus.define_Visitor()[0], Zeus.define_Visitor()[1], Zeus.define_Visitor()[2]))
    # getting value from customers as a third param of coffeeshops
    for i in range(5):
        coffeeshops.append(CoffeeShop(Zeus.define_CoffeeShop()[0], Zeus.define_CoffeeShop()[1],
                                      customers[randrange(len(customers))].getmark()))
    loop = True
    while loop:
        loop = menu(coffeeshops, customers)
    quit()


def menu(coffeeshops, customers):
    choice = int(input("""
                    Menu:
        Press 1 to show all the CoffeeShops
        Press 2 to show all the Customers
        Press 3 to show price of coffee in each CoffeeShop
        Press 4 to make Manager close a CoffeeShop for too high price ( you should find out what the price will be)
        Press 5 to QUIT"""))

    if choice == 1:
        for i in coffeeshops:
            print(i.name, ':\nPlace is ', i.place, '\nVisitors mark is', round(i.visitors_mark))
        return 1
    elif choice == 2:
        for i in customers:
            print(i.name, ':\nMood is ', i.mood, '\nAge is ', i.age)
        return 1
    elif choice == 3:
        for i in coffeeshops:
            print('Price is ', i.getprice())
        return 1
    elif choice == 4:
        price = int(input('Enter a price, that shouldn\'t be affordable for u:'))
        Manager(coffeeshops, price).delshop()
        return 1

    elif choice == 5:
        return 0


if __name__ == '__main__':
    main()
else:
    quit(print('Error!'))
