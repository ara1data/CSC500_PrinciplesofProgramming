# Step 1: ItemToPurchase Python Class
'''
Build the ItemToPurchase class with the following specifications:

Attributes
- item_name (string)
- item_price (float)
- item_quantity (int)

Default constructor
- Initializes item's name = "none", item's price = 0, item's quantity = 0

Method
- print_item_cost()

Example of print_item_cost() output:
Bottled Water 10 @ $1 = $10
'''
# ------------------------------>

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}")


# Step 2: Prompt User for Items Input
'''
In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.

Example:
- Item 1
-- Enter the item name: Chocolate Chips
-- Enter the item price: 3
-- Enter the item quantity: 1

- Item 2
-- Enter the item name: Bottled Water
-- Enter the item price: 1
-- Enter the item quantity: 10
'''
# ------------------------------>

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

# Step 3: Output Total Cost
'''
Add the costs of the two items together and output the total cost.

Example:
- TOTAL COST
-- Chocolate Chips 1 @ $3 = $3
-- Bottled Water 10 @ $1 = $10
- Total: $13

'''
# ------------------------------>

print("\nTOTAL COST")
item1.print_item_cost()
item2.print_item_cost()

total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print(f"Total: ${total_cost}")