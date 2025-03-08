# Part 1: Room numbers
ROOMS = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

# Part 2: Instructors
INSTRUCTORS = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

# Part 3: Meeting times
TIMES = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Menu for the user interface
def print_menu():
    """Prints the menu and gets the user's choice."""
    print("\nMENU")
    print("r - Get room number")
    print("i - Get instructor")
    print("m - Get meeting time")
    print("q - Quit")

    while True:
        choice = input("Choose an option: ")
        if choice in ('r', 'i', 'm', 'q'):
            return choice
        else:
            print("Invalid choice. Please try again.")

# Function that returns course information to the user
def get_course_info(course_number, rooms, instructors, times):
    """Retrieves and displays course information."""
    if course_number in rooms:
        print(f"Course: {course_number}")
        print(f"Room: {rooms[course_number]}")
        print(f"Instructor: {instructors[course_number]}")
        print(f"Meeting Time: {times[course_number]}")
    else:
        print("Course number not found.")

def main():
    """Main function to run the program."""

    while True:
        choice = print_menu()

        if choice == 'r':
            course_number = input("Enter course number: ").upper()
            if course_number in ROOMS:
                print(f"Room: {ROOMS[course_number]}")
            else:
                print("Course number not found.")
        elif choice == 'i':
            course_number = input("Enter course number: ").upper()
            if course_number in INSTRUCTORS:
                print(f"Instructor: {INSTRUCTORS[course_number]}")
            else:
                print("Course number not found.")
        elif choice == 'm':
            course_number = input("Enter course number: ").upper()
            if course_number in TIMES:
                print(f"Meeting Time: {TIMES[course_number]}")
            else:
                print("Course number not found.")
        elif choice == 'q':
            break

if __name__ == "__main__":
    main()
