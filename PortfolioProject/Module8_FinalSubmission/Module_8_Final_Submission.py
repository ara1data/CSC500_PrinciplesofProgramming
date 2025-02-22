# Part 1 from Milestone 1: ItemToPurchase Python Class
## Edits made to the class during Milestone 2 (noted in comments)

class ItemToPurchase:
    # Added item_description attribute to the class (Milestone 2)
    def __init__(self, item_name="none", item_description="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        # Added item_description attribute to the class (Milestone 2)
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        # Added item_description to the print statement (Milestone 2)
        print(f"{self.item_name}: {self.item_description} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}")

# Part 2 from Milestone 1: Prompt User for Items Input
## Removed this part from the code base because it will be completed in the Shopping Cart class of milestone 2.
'''
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
'''

# Part 3 from Milestone 1: Output Total Cost
## Removing this part from the code base because items will be printed in step 6 of milestone 2.
'''
print("\nTOTAL COST")
item1.print_item_cost()
item2.print_item_cost()

total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print(f"Total: ${total_cost}")
'''

# Part 4 from Milestone 2: ShoppingCart Python Class

class ShoppingCart:
    # Section 1: Parameterized constructor
    def __init__(self, customer_name="none", current_date="February 22, 2025"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Section 2: Add_item
    def add_item(self, item):
        self.cart_items.append(item)

    # Section 3: Remove_item
    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    # Section 4: Modify_item
    def modify_item(self, item_to_modify):
        found = False
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                if item_to_modify.item_price != 0:
                    item.item_price = item_to_modify.item_price
                if item_to_modify.item_description != "none":
                    item.item_description = item_to_modify.item_description
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    # Section 5: Get_num_items_in_cart
    def get_num_items_in_cart(self):
        total_items = 0
        for item in self.cart_items:
            total_items += item.item_quantity
        return total_items

    # Section 6: Get_cost_of_cart
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost
    
    # Section 7: Print_total
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        for item in self.cart_items:
            item.print_item_cost()
        print(f"Total: ${self.get_cost_of_cart()}")

    # Section 8: Print_descriptions
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


# Part 5 from Milestone 2: Print Menu Function

def print_menu(cart):
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")

    while True:
        choice = input("Choose an option: ")
        if choice in ('a', 'r', 'c', 'i', 'o', 'q'):
            return choice
        else:
            print("Invalid choice. Please try again.")

# Part 6 from Milestone 2: Print ShoppingCart Menu Function

if __name__ == "__main__":
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name, current_date)

    while True:
        choice = print_menu(cart)

        if choice == 'a':
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            new_item = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            cart.add_item(new_item)

        elif choice == 'r':
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove: ")
            cart.remove_item(item_name)

        elif choice == 'c':
            print("CHANGE ITEM QUANTITY")
            item_name = input("Enter the item name: ")
            quantity = int(input("Enter the new quantity: "))
            modify_item = ItemToPurchase(item_name=item_name, item_quantity=quantity)
            cart.modify_item(modify_item)

        elif choice == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif choice == 'o':
            print("OUTPUT SHOPPING CART")
            cart.print_total()

        elif choice == 'q':
            break

# Part 7 Assignment Prompt
'''
In the main section of your code, prompt the user for a customer's name and today's date. 
Output the name and date. Create an object of type ShoppingCart.

Example:
Enter customer's name: John Doe
Enter today's date: February 1, 2020
Customer name: John Doe
Today's date: February 1, 2020
'''




# Part 8 Assignment Prompt
'''
Implement Add item to cart menu option.

Example:
ADD ITEM TO CART
Enter the item name: Nike Romaleos
Enter the item description: Volt color, Weightlifting shoes
Enter the item price: 189
Enter the item quantity: 2
'''





# Part 9 Assignment Prompt
'''
Implement remove item menu option.

Example:
REMOVE ITEM FROM CART
Enter name of item to remove: Chocolate Chips
'''





# Part 10 Assignment Prompt
'''
Implement Change item quantity menu option. 
Hint: Make new ItemToPurchase object before using ModifyItem() method.

Example:
CHANGE ITEM QUANTITY
Enter the item name: Nike Romaleos
Enter the new quantity: 3
'''



