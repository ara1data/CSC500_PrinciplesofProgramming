# Part 1: Assignment Prompt
'''
Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. 
The program should first ask for the number of years. The outer loop will iterate once for each year. 
The inner loop will iterate twelve times, once for each month. 
Each iteration of the inner loop will ask the user for the inches of rainfall for that month. 
After all iterations, the program should display the number of months, the total inches of rainfall, 
and the average rainfall per month for the entire period.
'''
# -------------------->

def calculate_average_rainfall():
    """Calculates and displays the average rainfall over a period of years."""

    # Ask user for number of years with error handling
    try:
        num_years = int(input("Enter the number of years: "))
        if num_years <= 0:
            raise ValueError("Number of years must be greater than zero.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    # Define variables to store total rainfall and total months
    total_rainfall = 0
    total_months = 0

    # Iterate for each year
    for year in range(num_years):
        print(f"\nEnter rainfall data for year {year + 1}:")
        for month in range(12):
            while True:  # Input validation loop
                # Iterate for each month and ask user for monthly rainfall
                try:
                    rainfall = float(input(f"Enter rainfall for month {month + 1} (in inches): "))
                    if rainfall < 0:
                        raise ValueError("Rainfall cannot be negative.")
                    break  # Exit loop if input is valid
                except ValueError as e:
                    print(f"Invalid input: {e}")

            # Counters: update total rainfall and total months
            total_rainfall += rainfall
            total_months += 1

    # Final calculations and output
    if total_months > 0:
        # Calculate average rainfall
        average_rainfall = total_rainfall / total_months
        
        # Display results to users
        print("\nRainfall Summary:")
        # Display the number of months
        print(f"Total Months: {total_months}")
        # Display total inches of rainfall
        print(f"Total Rainfall: {total_rainfall:.2f} inches")
        # Display average rainfall per month over period
        print(f"Average Rainfall per Month: {average_rainfall:.2f} inches")
    else:
        print("No rainfall data entered.")

# Call the main function
if __name__ == "__main__":
    calculate_average_rainfall()