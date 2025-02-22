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
## Removed this part from the code base because it will be completed in the Shopping Cart class of Milestone 2.
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

# Part 4: ShoppingCart Python Class
'''
Build the ShoppingCart class with the following data attributes and related methods. 
Note: Some can be method stubs (empty methods) initially, to be completed in later steps.

Section 1
Parameterized constructor, which takes the customer name and date as parameters:
- Attributes
- customer_name (string) - Initialized in default constructor to "none"
- current_date (string) - Initialized in default constructor to "January 1, 2020"
- cart_items (list)
- Methods

Section 2
- add_item()
-- Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.

Section 3
- remove_item()
-- Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
-- If item name cannot be found, output this message: Item not found in cart. Nothing removed.

Section 4
- modify_item()
-- Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
-- If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity. If not, modify item in cart.
-- If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.

Section 5
- get_num_items_in_cart()
-- Returns quantity of all items in cart. Has no parameters.

Section 6
- get_cost_of_cart()
-- Determines and returns the total cost of items in cart. Has no parameters.

Section 7
- print_total()
-- Outputs total of objects in cart.
-- If cart is empty, output this message: SHOPPING CART IS EMPTY

Section 8
- print_descriptions()
-- Outputs each item's description.

Example of print_total() output:
John Doe's Shopping Cart - February 1, 2020
Number of Items: 8
Nike Romaleos 2 @ $189 = $378
Chocolate Chips 5 @ $3 = $15
Powerbeats 2 Headphones 1 @ $128 = $128
Total: $521

Example of print_descriptions() output:
John Doe's Shopping Cart - February 1, 2020
Item Descriptions
Nike Romaleos: Volt color, Weightlifting shoes
Chocolate Chips: Semi-sweet
Powerbeats 2 Headphones: Bluetooth headphones
'''

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

# Part 5: Print Menu Function
'''
In the main section of your code, implement the print_menu() function. 
print_menu() has a ShoppingCart parameter and outputs a menu of options to manipulate the shopping cart. 
Each option is represented by a single character. Build and output the menu within the function.

If an invalid character is entered, continue to prompt for a valid choice. 
Hint: Implement Quit before implementing other options. Call print_menu() in the main() function. 
Continue to execute the menu until the user enters q to Quit.

Example:
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option:
'''

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

# Part 6: Print ShoppingCart Menu Function
'''
Implement Output shopping cart menu option. Implement Output item's description menu option.

Example of shopping cart menu option:
OUTPUT SHOPPING CART
John Doe's Shopping Cart - February 1, 2020
Number of Items: 8
Nike Romaleos 2 @ $189 = $378
Chocolate Chips 5 @ $3 = $15
Powerbeats 2 Headphones 1 @ $128 = $128
Total: $521

Example of item description menu option.
OUTPUT ITEMS' DESCRIPTIONS
John Doe's Shopping Cart - February 1, 2020
Item Descriptions
Nike Romaleos: Volt color, Weightlifting shoes
Chocolate Chips: Semi-sweet
Powerbeats 2 Headphones: Bluetooth headphones

Fix any issues from milestone 2 submission prior to submitting the Portfolio Project.
'''

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