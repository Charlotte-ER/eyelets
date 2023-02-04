### CALCULATES MEASUREMENTS FOR PLACEMENT OF EYELETS TO LACE A MEDIEVAL GARMENT
### for Mum, love Charlotte 02/05/2022


def main():
    opening = round(float(input('How long is your opening? ')),1)
    position = round(float(input('How far down from the top edge do you want your first eyelet to be? ')),1)
    number = int(input('How many cross-laces do you want (excluding top and bottom laces)? '))

    standard = calculate_standard_distance_between_eyelets(opening, position, number)

    print(create_instructions(opening, position, standard, number))
    print(create_diagram(standard, number))


def calculate_standard_distance_between_eyelets(opening, position, number):
    return round(((opening - (position * 2)) / (number + 0.5)),1)


def title(title):
    return f'\n{"-" * 100} \n{title.upper()}\n{"-" * 100}\n\n'


def create_instructions(opening, position, standard, number):
    return (f'{title("Instructions")}'

    f'Length of Opening: {opening}\n'
    f'Position of first eyelet: {position} down from top edge\n'
    f'Number of diagonal cross-laces: {number}\n\n'

    f'Starting from the top edge of your opening, mark eyelets {position} down from the top, on both sides.\n'
    f'Starting from the bottom edge of your opening, mark eyelets {position} up from the bottom, on both sides.\n\n'
    f'On the LEFT hand side of the opening:\n'
    f'\tmark an eyelet {standard/2} down from the first eyelet\n'
    f'\tmark the other {number-1} eyelets, each {standard} down from the eyelet above.\n'
    f'\nOn the RIGHT hand side of the opening:\n'
    f'\tmark an eyelet {standard} down from the first eyelet\n'
    f'\tmark the other {number-1} eyelets, each {standard} down from the eyelet above.\n'
    f'\tthe gap between the bottom two eyelets on the right should measure {standard/2}.\n')


def create_diagram(standard, number):
    heading = f'{title("Diagram")}'
    first_row = f'\tX\tX\n\t{(standard)/2}\t|\n'
    laces = ''
    last_row = f'\t|\t{(standard)/2}\n\tX\tX\n'
    footer = f'\n{"-"*100}'

    for i in range(number):
        laces = laces + (f'\tX\t{(standard)}\n\t|\t|\n\t{(standard)}\tX\n')
        if i < (number-1):
            laces = laces + (f'\t|\t|\n')

    return heading + first_row + laces + last_row + footer


if __name__ == "__main__":
    main()
