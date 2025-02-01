# Part 1 Assignment Prompt
'''
Write a program that calculates the total amount of a meal purchased at a restaurant. The program 
should ask the user to enter the charge for the food and then calculate the amounts with an 
18 percent tip and 7 percent sales tax. Display each of these amounts and the total price.
'''
# ---------------------------------------------

# Define function for this calculating the bill that includes error handling for user input
def calculate_total_bill():

    # Try function that includes error handling for user input
    try:
        # Prompt user for the pre-tax, pre-tip price of food & drink
        food_drink_price = float(input("How much was your food and drink? $"))
        
        # Error handling for negative numbers
        if food_drink_price < 0:
            raise ValueError("The amount must be a number greater than zero.")
        
        # Calculate tip (18%)
        tip = food_drink_price * 0.18
        # Calculate sales tax (7%)
        sales_tax = food_drink_price * 0.07

        # Calculate total price
        total_price = food_drink_price + tip + sales_tax

        # Display results
        print(f"\nFood charge: ${food_drink_price:.2f}")
        print(f"Tip (18%): ${tip:.2f}")
        print(f"Sales tax (7%): ${sales_tax:.2f}")
        print(f"Total price: ${total_price:.2f}")

    # Error handling for invalid inputs
    except ValueError as e:
        print(f"Invalid input: {e}")
        print("Invalid input: Please enter a valid number.")
        return calculate_total_bill()
    
    # Error handling for all other exceptions
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to run the program
calculate_total_bill()