# Part 1 from Milestone 1

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}")

# Part 2 from Milestone 1

if __name__ == "__main__":
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()

    print("Item 1")
    item1.item_name = input("Enter the item name: ")
    item1.item_price = float(input("Enter the item price: "))
    item1.item_quantity = int(input("Enter the item quantity: "))

    print("Item 2")
    item2.item_name = input("Enter the item name: ")
    item2.item_price = float(input("Enter the item price: "))
    item2.item_quantity = int(input("Enter the item quantity: "))

# Part 3 from Milestone 1

print("\nTOTAL COST")
item1.print_item_cost()
item2.print_item_cost()

total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print(f"Total: ${total_cost}")

# Part 4 from Milestone 2



# Part 5 from Milestone 2



# Part 6 from Milestone 2



# Part 7 Assignment Prompt
'''
In the main section of your code, prompt the user for a customer's name and today's date. Output the name and date. Create an object of type ShoppingCart.

Example:
Enter customer's name:
John Doe
Enter today's date:
February 1, 2020
Customer name: John Doe
Today's date: February 1, 2020
'''




# Part 8 Assignment Prompt
'''
Implement Add item to cart menu option.

Example:
ADD ITEM TO CART
Enter the item name:
Nike Romaleos
Enter the item description:
Volt color, Weightlifting shoes
Enter the item price:
189
Enter the item quantity:
2
'''





# Part 9 Assignment Prompt
'''
Implement remove item menu option.

Example:
REMOVE ITEM FROM CART
Enter name of item to remove:
Chocolate Chips
'''





# Part 10 Assignment Prompt
'''
Implement Change item quantity menu option. Hint: Make new ItemToPurchase object before using ModifyItem() method.

Example:
CHANGE ITEM QUANTITY
Enter the item name:
Nike Romaleos
Enter the new quantity:
3
'''



