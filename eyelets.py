### CALCULATES MEASUREMENTS FOR PLACEMENT OF EYELETS TO LACE A MEDIEVAL GARMENT
### for Mum, love Charlotte 02/05/2022


def main():
    opening, position, number = get_user_input()

    standard = calculate_standard_distance(opening, position, number)
    
    print_instructions(position, number, standard)
    print_diagram(standard, number)


def get_user_input():
    # Get length of opening
    opening = round(float(input("How long is your opening? ")),1)

    # Get desired start and end position
    position = round(float(input("How far down from the top edge do you want your first eyelet to be? ")),1)

    # Get desired number of laces
    number = int(input("How many cross-laces do you want (excluding top and bottom laces)? "))

    return opening, position, number


def calculate_standard_distance(opening, position, number):
    # Calculate standard distance between each eyelet
    return round(((opening - (position * 2)) / (number + 0.5)),1)


def print_instructions(position, number, standard):
    # Output Instructions
    print("\n---------------------------------------------------------------------------------------------------------")
    print("INSTRUCTIONS")
    print("---------------------------------------------------------------------------------------------------------")

    print(f"\nStarting from the top edge of your opening, mark eyelets {position} down from the top, on both sides.")
    print(f"Starting from the bottom edge of your opening, mark eyelets {position} up from the bottom, on both sides.")
    print(f"\nOn the LEFT hand side of the opening:")
    print(f"\tmark an eyelet {standard/2} down from the first eyelet")
    print(f"\tmark the other {number-1} eyelets, each {standard} down from the eyelet above.")
    print(f"\nOn the RIGHT hand side of the opening:")
    print(f"\tmark an eyelet {standard} down from the first eyelet")
    print(f"\tmark the other {number-1} eyelets, each {standard} down from the eyelet above.")
    print(f"\tthe gap between the bottom two eyelets on the right should measure {standard/2}.")


def print_diagram(standard, number):
    # Output Diagram
    print("\n---------------------------------------------------------------------------------------------------------")
    print("DIAGRAM")
    print("---------------------------------------------------------------------------------------------------------")
    # First row
    print('\n')
    print(f"\tX\tX")
    print(f"\t{(standard)/2}\t|")

    # Laces
    for i in range(number):
        print(f"\tX\t{(standard)}")
        print(f"\t|\t|")
        print(f"\t{(standard)}\tX")
        if i < (number-1):
            print(f"\t|\t|")

    # Last row
    print(f"\t|\t{(standard)/2}")
    print(f"\tX\tX")

    print("---------------------------------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
