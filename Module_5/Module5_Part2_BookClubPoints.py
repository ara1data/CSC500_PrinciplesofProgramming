# Part 2: Assignment Prompt
'''
The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month. 

The points are awarded as follows:
- If a customer purchases 0 books, they earn 0 points.
- If a customer purchases 2 books, they earn 5 points.
- If a customer purchases 4 books, they earn 15 points.
- If a customer purchases 6 books, they earn 30 points.
- If a customer purchases 8 or more books, they earn 60 points.

Write a program that asks the user to enter the number of books that they have purchased this month and then display 
the number of points awarded.
'''

# -------------------->

# Outline point categories
def calculate_bookstore_points(num_books):
    """Calculates bookstore points based on the number of books purchased."""
    # Initialize points variable with if and elif statements
    if num_books == 0 and num_books < 2: # Values 0 and 1
        points = 0
    elif num_books == 2 or num_books < 4: # Values 2 and 3
        points = 5
    elif num_books == 4 or num_books < 6: # Values 4 and 5
        points = 15
    elif num_books == 6 or num_books < 8: # Values 6 and 7
        points = 30
    elif num_books >= 8: # Values 8 and above
        points = 60
    else:  # Catch-all for invalid input
      points = "Invalid number of books. Must be a whole number greater than or equal to 0."

    return points

# Main function to get user input and display points
def main():
    """Gets user input and displays the calculated points."""

    while True:
        try:
            num_books = int(input("Enter the number of books purchased this month: "))
            if num_books < 0:
                raise ValueError("Number of books cannot be negative.")
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Invalid input: {e}")

    points = calculate_bookstore_points(num_books)
    print(f"Points awarded: {points}")

# Call the main function
if __name__ == "__main__":
    main()