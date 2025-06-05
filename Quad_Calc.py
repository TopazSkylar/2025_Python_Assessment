
# functions go below
def to_continue():
    """Breaks up the sudden information by prompting user to
    interact"""
    input("Press any key to continue...")


def line_maker(line):
    """Makes lines"""
    print(f"{line * 10}")

def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")

def yes_no(question, valid_ans_list=('yes', 'no'), num_letters=1):
    """Checks that users enter the full word or then, letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # checks user response to question
            # only accepts yes or no
            if response == item:
                return item

            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print("Please enter either yes or no")

def show_instructions():
    make_statement("Instructions", "ℹ️")
    print('''
This is a quadratic calculator, you will be prompted to enter the values of a, b and c 
This will correspond to the x^2, x and constant value of the quadratic 

''')
    line_maker("--")

def num_check(question):
    while True:

        try:
            response = float(input(question))
            return response

        except ValueError:
            print("Please enter an integer")

def find_equation():
    """Finds and solves the equation for the quadratic"""

    ask_a = "what is your a (x^2) value? "
    ask_b = "what is your b (x) value? "
    ask_c = "what is your c (constant) value? "

    a = num_check(ask_a)
    b = num_check(ask_b)
    c = num_check(ask_c)

    print()
    # formats the equation in order to negate the use of brackets
    if b < 0 < c:
        make_statement(f"{a}x^2{b}x+{c}", "*")
    if b > 0 > c:
        make_statement(f"{a}x^2+{b}x{c}", "*")
    if c < 0 and b < 0:
        make_statement(f"{a}x^2{b}x{c}", "*")
    if c > 0 and b > 0:
        make_statement(f"{a}x^2+{b}x+{c}", "*")


    print()

    print()
    # makes sure that the user wishes to solve the equation they just entered
    # (ERROR PREVENTION)
    confirmation = yes_no("Is this the equation you wish to solve?")
    print()
    if confirmation == "no":
        find_equation()

    else:
        # The quadratic formula that calculates the two results
        negative_result = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        positive_result = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

        discriminant = b ** 2 - 4 * a * c

        # checks if the quadratic is able to be calculated
        if discriminant < 0:
            print(f"Calculating the discriminant of ({b})^2-4({a})({c}) is less than zero,"
                  f" thus this equation has complex roots, and is unable to be solved using this "
                  f"calculator")
            return
        if discriminant == 0:
            print(f"The discriminant of ({b})^2-4({a})({c}) equals zero, meaning that this a perfect "
                  f"square with the same two roots")
        else:
            print(f"The discriminant of ({b})^2-4({a})({c}) is greater than zero, meaning that there "
                  f"are two real unequal roots")

        print()
        to_continue()
        # The information that the user gets about their solved equations
        print(f"\r(-({b})±(({b})^2 - 4({a})({c}))^1/2) / 2({a}) gives the answers of")
        print()
        # first x result
        make_statement(f"x = {negative_result:.2f}", "*")
        print()
        # second x result
        make_statement(f"x = {positive_result:.2f}", "*")

        print()
        to_continue()
        print()

        root_1 = negative_result/-1
        if root_1 < 0:
            final_1 = f"x{root_1}"
        else:
            final_1 = f"x+{root_1}"

        root_2 = positive_result / -1
        if root_2 < 0:
           final_2 = f"x{root_2}"
        else:
            final_2 = f"x+{root_2}"


        print("\rThus, your roots for this quadratic are; ")
        print()
        make_statement(f"{final_1}", "*")
        print()
        make_statement(f"{final_2}", "*")
        print()

# main routine goes here

make_statement("Quadratic calculator", "-")

while True:
    # instructions asker
    instructions = yes_no("Do you want to read the instructions? ")
    if instructions == "yes":
        show_instructions()

    find_equation()

    again = yes_no("Do you wish to solve another quadratic? ")
    if again == "yes":
        find_equation()
    else:
        break
print()
# end
print("Thank you for using the Quadratic Calculator")






