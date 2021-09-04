# DSC 510
# week 11
# Programming Assignment Week 11
# Created a cash register program by using OPPs concepts that has a class called cash register
# The program will print the total number of items in the cart and the total $ amount of the cart
# Author Theodore Koby-Hercsky
# 05/21/2021


# Change Control Log:
# Change#:1
# Change(s) Made:
# Author: Theodore Koby-Hercsky
# Change Approved by: Theodore Koby-Hercsky
# Date Moved to Production: 05/21/2021

import locale
# Called a customer to my register and welcomed them
print("We have an opening on lane six!!!""Welcome to my cash register!")

# I created a class titled Cash Register that has an instant item that adds items.
# While also having two getter methods for price and count


class CashRegister:
    def __init__(self):
        self.Total_Price = 0
        self.Item_Count = 0

    def __addItem__(self, price):
        self.Total_Price = self.Total_Price + price
        self.Item_Count += 1

    def __getCount__(self):
        return self.Item_Count

    def __getTotal__(self):
        locale.setlocale(locale.LC_ALL, 'en_US.utf-8')
        return locale.currency(self.Total_Price, symbol=True)


# In the main function I have a while loop that asks the user for the next price of the item.
# while also asking if they are done which will lead to an if statement
# that will print out the amount of items and the cost.

def main():
    my_register = CashRegister()
    items_price = []
    while items_price != 'register total':
        items_price = input("What is the items price? "
                            "\nIf done please type 'register total' for the total: ").strip().strip('$').lower()
        while True:
            if items_price == 'register total':
                break
            try:
                items_price = float(items_price)
                break
            except ValueError:
                items_price = input('invalid entry! Type the items price '
                                    'or register total: ').strip().strip('$').lower()

        if items_price == 'register total':
            print(f'You have {my_register.__getCount__()} items'
                  f' that total {my_register.__getTotal__()}')
        my_register.__addItem__(items_price)


main()
