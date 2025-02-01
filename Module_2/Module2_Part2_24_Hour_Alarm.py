# Part 2 Assignment Prompt
'''
Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
Write a Python program to solve the general version of the above problem. 
Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm. 
Your program should output what the time will be on a 24-hour clock when the alarm goes off.
'''
# ---------------------------------------------

# Define function that calculates alarm time that includes error handling for user input
def twenty_four_hour_alarm():
    # Ask user for current time
    try:
        # Ask user for current time
        current_time = int(input("Enter the current time (only in hours), 00-23): "))
        
        # Error handling for invalid time
        if current_time < 0 or current_time > 23:
            # Raise ValueError if the time is not between 0 and 23
            raise ValueError("The time must be a number between 0 and 23.")
    
    # Error handling for invalid inputs
    except ValueError as e:
        # Display error message
        print(f"Invalid input: {e}")
        # Return to the beginning of the function
        return twenty_four_hour_alarm()
    
    # Error handling for all other exceptions
    try:
        # Ask user for number of hours to wait for the alarm
        wait_time = int(input("Enter the number of hours to wait for the alarm: "))

        # Error handling for negative numbers
        if wait_time < 0:
            # Raise ValueError if the number of hours is negative
            raise ValueError("The number of hours must be a positive number.")
        
    # Error handling for invalid inputs
    except ValueError as e:
        # Display error message
        print(f"Invalid input: {e}")
        # Return to the beginning of the function
        return twenty_four_hour_alarm()

    # Calculate alarm time
    alarm_time = (current_time + wait_time) % 24

    # Display result
    print(f"\nThe alarm will go off at {alarm_time:02d}:00 on the 24-hour clock.")

# Call the function to run the program
twenty_four_hour_alarm()