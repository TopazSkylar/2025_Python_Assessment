from prettytable import PrettyTable

# Lists
factors_list = []
rr_raw = []
rr_final = []
rr_count = []
# Table formatting for display
base_table = PrettyTable(["x^2", "x", "c", "0", "Comments"])
base_table.add_row(["", "", "", "", "<---- This top column contains the constants of the cubic"])
base_table.add_row(["", "", "", "", "<-- This will be the value you are adding to the above column"])
base_table.add_row(["", "", "", "", "<---- This will be the values for the quadratic you will get"])


# functions go below
def to_continue():
    """Breaks up the sudden information by prompting user to
    interact"""
    print()
    input("Press Enter to continue...")
    print("\n" * 30)
    print("-" * 144)

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
    print()
    make_statement("Instructions", "ℹ️")
    print('''
This is a cubic calculator, 
You will first be prompted to decide the amount of questions you would like to ask 
(Due to this being intended for year 13 students there is no way to quit 
as I expect the question amounts to be reasonable)
You will be prompted to enter integers as values of a, b, c and d
This will correspond to the x^3, x^2, x and constant value of the cubic 
This calculator will not be able to calculate complex roots
This calculator is intended to walk the user through the steps to solve these cubics 


''')
    to_continue()

def num_check(question):
    """Can only enter integers"""
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer")

def format_term(co, variable):
    """Makes things pretty in terms of the signs"""
    if co == 0:
        return ""
    sign = "+" if co > 0 else "-"
    abs_co = abs(co)
    if variable:
        term = f"{abs_co}{variable}"
    else:
        term = f"{abs_co}"
    return f"{sign}{term}"

def format_equation(a, b, c, d):
    """Correct formatting in the cubic """
    eq = f"{a}x^3"
    eq += format_term(b, "x^2")
    eq += format_term(c, "x")
    eq += format_term(d, "")
    return eq

def format_equation_quad(a, b, c):
    """Formats correct signage in the quad"""
    eq = f"{a}x^2"
    eq += format_term(b, "x")
    eq += format_term(c, "")
    return eq

def quad_solver(x, y, z):
    """Quad calc condensed into one function"""
    discriminant = y ** 2 - 4 * x * z
    negative_result = (-y - (y ** 2 - 4 * x * z) ** 0.5) / (2 * x)
    positive_result = (-y + (y ** 2 - 4 * x * z) ** 0.5) / (2 * x)
    # checks if the quadratic is able to be calculated
    if discriminant < 0:
        print(f"""
Calculating the discriminant of ({y})^2-4({x})({z}) is less than zero,
thus this equation has complex roots, and is unable to be solved using this 
calculator
                        """)
        return
    if discriminant == 0:
        print(f"""
The discriminant of ({y})^2-4({x})({z}) equals zero, meaning that this a perfect
square with the same two roots
                        """)
    else:
        print(f"""
The discriminant of ({y})^2-4({x})({z}) is greater than zero, meaning that there
are two real unequal roots
                        """)


    # more formatting for prettiness
    root_1 = negative_result / -1
    if root_1 < 0:
        final_1 = f"x{root_1}"
    else:
        final_1 = f"x+{root_1}"

    root_2 = positive_result / -1
    if root_2 < 0:
        final_2 = f"x{root_2}"
    else:
        final_2 = f"x+{root_2}"

    print("\rThus, your roots for this cubic are; ")
    print()
    make_statement(f"{final_1}", "*")
    print()
    make_statement(f"{final_2}", "*")
    print()
    # will always be (x+0) because it is a quad and this would be 0
    make_statement(f"x+0", "*")
    print()

def find_factors(value):
    """returns the factors (+ and -) of a number"""
    if value == 0:  # making sure the program doesn't send anything if there is this factor
        return [0]

    # goes through every number between 1 and num, and divides num by it to get remainder
    factors=[]
    for f in range(1, abs(value) + 1):

        # if remainder is equal to 0, append the factor
        if value % f == 0:
            factors.append(f)

    return factors

def find_equation():
    questions_answered = 0

    questions_asked = num_check("How many questions would you like? ")

    for q in range(questions_asked):
        while questions_answered < questions_asked:
            # creates a boundary that automatically ends after answering enough questions
            question_heading = f"\n🐦‍🔥🐦‍🔥🐦‍🔥 Question {questions_answered + 1} of {questions_asked} 🐦‍🔥🐦‍🔥🐦‍🔥"

            print(question_heading)

            ask_a = "what is your a (x^3) value? "
            ask_b = "what is your b (x^2) value? "
            ask_c = "what is your c (x) value? "
            ask_d = "what is your d (constant) value? "


            # if user hasn't quit
            a = num_check(ask_a)
            b = num_check(ask_b)
            c = num_check(ask_c)
            d = num_check(ask_d)

            print()
            # formats the equation in order to negate the use of brackets
            eq = format_equation(a, b, c, d)
            make_statement(eq, "*")

            print()
            # makes sure that the user wishes to solve the equation they just entered
            # (ERROR PREVENTION)
            confirmation = yes_no("Is this the equation you wish to solve?")
            print()
            if confirmation == "no":
                to_continue()
                continue

            else:
                to_continue()
                # shows the user what to how to solve the quadratic equation and formats them correctly
                eq2 = format_equation_quad(b, c, d)
                eq3 = format_equation_quad(a, b, c)
                # if a = 0 make quad
                if a == 0:
                    print("Due to the a value being 0, the equation becomes a quadratic")
                    print()
                    print(f"{eq2}")
                    to_continue()
                    quad_solver(b, c, d)
                    questions_answered += 1
                    continue
                # if d = 0 make quad
                if d == 0:
                    print("Due to the d value being 0, you are able to factorise out x, and simply make it a quadratic")
                    print()
                    print(f"x({eq3})")
                    to_continue()
                    quad_solver(a, b, c)
                    questions_answered += 1
                    continue
                # the discriminant for a cubic will indicate whether there are complex roots
                discriminant_check = (18 * a * b * c * d - 4 * (b ** 3) * d + (b ** 2) * (c ** 2)
                                      - 4 * a * (c ** 3) - 27 * (a ** 2) * (d ** 2))

                if discriminant_check > 0:
                    square_num = discriminant_check ** 0.5
                    if square_num == int(square_num):
                        print(
                            """The cubic discriminant equation has found the discriminant at > 0 but is a square number, 
                            which indicates real roots which can be solved using this calculator"""
                        )
                    else:
                        print(
                        """The cubic discriminant equation has found the discriminant at > 0 and not a square number, 
                        indicating complex roots which cannot be solved using this calculator"""
                        )
                        questions_answered += 1
                        continue

                elif discriminant_check == 0:
                    print(
                        "Utilising the cubic discriminant equation has these values at = 0, indicating repeated real roots")
                elif discriminant_check < 0:
                    print(
                        "Utilising the cubic discriminant equation has these values at < 0, "
                        "indicating complex roots which cannot be solved using this calculator"
                    )
                    questions_answered += 1
                    continue

                to_continue()


                find_factors(d)

                # information for the user
                print(f"Step 1. Factors of {d} are ± {find_factors(d)}")
                # due to 1 and -1 being a factor in every integer, they can automatically be the lowest possible common factors
                root_1 = 0
                if a * (-1) ** 3 + b * (-1) ** 2 + c * (-1) + d != 0:
                    root_1 = -1
                elif a * 1 ** 3 + b * 1 ** 2 + c * 1 + d != 0:
                    root_1 = 1

                # for every item in the list of factors
                for item in range(find_factors(d)[0], find_factors(d)[-1]):
                    # if substituting into the equation equals to 0
                    if a * item ** 3 + b * item ** 2 + c * item + d == 0:
                        root_1 = item

                    # otherwise search for negative factors
                    else:
                        # negative factors of d
                        neg_factors_list = [-x for x in find_factors(d)]
                        for i in range(neg_factors_list[0], neg_factors_list[-1]):
                            if a * i ** 3 + b * i ** 2 + c * i + d == 0:
                                root_1 = i

                # explains to the user how to come to the first factor
                print(f"through substituting until equation = 0, {root_1:.2f} is applicable as a factor ")
                # formating

                if root_1 < 0:
                    display = f"x+{abs(root_1):.2f}"
                else:
                    display = f"x-{abs(root_1):.2f}"

                make_statement(f"This means your first factor of {eq} is {display}", "*")
                print()
                to_continue()
                print(f"Step 2. With {root_1} being a factor, synthetic division can be used")

                # Table for formatting calculations for x^2
                calc_table_x2 = PrettyTable(["x^2", "x", "c", "0"])
                calc_table_x2.add_row([f"{a}", "", "", ""])
                calc_table_x2.add_row(["0", "", "", ""])
                calc_table_x2.add_row([f"{a}", "", "", ""])
                # Table for x
                calc_table_x = PrettyTable(["x^2", "x", "c", "0"])
                calc_table_x.add_row([f"{a}", f"{b}", "", ""])
                calc_table_x.add_row(["0", f"{a * root_1}", "", ""])
                calc_table_x.add_row([f"{a}", f"{b + a * root_1}", "", ""])
                # Table for c
                calc_table_c = PrettyTable(["x^2", "x", "c", "0"])
                calc_table_c.add_row([f"{a}", f"{b}", f"{c}", ""])
                calc_table_c.add_row(["0", f"{a * root_1}", f"{(b + a * root_1) * root_1}", ""])
                calc_table_c.add_row([f"{a}", f"{b + a * root_1}", f"{c + (b + a * root_1) * root_1}", ""])
                # Table for 0
                calc_table_0 = PrettyTable(["x^2", "x", "c", "0"])
                calc_table_0.add_row([f"{a}", f"{b}", f"{c}", f"{d}"])
                calc_table_0.add_row(
                    ["0", f"{a * root_1}", f"{(b + a * root_1) * root_1}", f"{(c + (b + a * root_1) * root_1) * root_1}"])
                calc_table_0.add_row([f"{a}", f"{b + a * root_1}", f"{c + (b + a * root_1) * root_1}",
                                      f"{d + (c + (b + a * root_1) * root_1) * root_1}"])

                a2 = a
                b2 = b + a * root_1
                c2 = c + (b + a * root_1) * root_1
                # The quadratic formula that calculates the two results
                negative_result = (-b2 - (b2 ** 2 - 4 * a2 * c2) ** 0.5) / (2 * a2)
                positive_result = (-b2 + (b2 ** 2 - 4 * a2 * c2) ** 0.5) / (2 * a2)

                print()
                to_continue()
                # Step-by-step walkthrough on how to make the table to get a quadratic for the final 2 roots
                print("Step 3. Lay out a table like the following ")
                print(base_table)
                print()
                to_continue()
                print("Step 4. Take your x^3 constant, this will be your result for your first column")
                print(calc_table_x2)
                print()
                to_continue()
                print(f"""
            Step 5. Take your x^2 constant to the next column across and add to it the product of
            your previous result and the factor (e.g {a}*{root_1})
                    """)
                print(calc_table_x)
                print()
                to_continue()
                print("Step 6. Repeat the previous step accordingly\n")
                print(calc_table_c)
                print()
                to_continue()
                print("Step 7. Your final result should be 0\n")
                print(calc_table_0)
                # The information that the user gets about their solved equations
                print(f"\r(-({b2})±(({b2})^2 - 4({a2})({c2}))^1/2) / 2({a2}) gives the answers of")
                print()
                # first x result
                make_statement(f"x = {negative_result:.2f}", "*")
                print()
                # second x result
                make_statement(f"x = {positive_result:.2f}", "*")

                print()
                to_continue()
                print()
                # correct formatting
                root_2 = negative_result / -1
                if root_2 < 0:
                    final_1 = f"x{root_2:.2f}"
                else:
                    final_1 = f"x+{root_2:.2f}"

                root_3 = positive_result / -1
                if root_3 < 0:
                    final_2 = f"x{root_3:.2f}"
                else:
                    final_2 = f"x+{root_3:.2f}"
                # displays all the roots after solving
                print("\rThus, your roots for this cubic are; ")
                print()
                make_statement(f"{display}", "*")
                print()
                make_statement(f"{final_1}", "*")
                print()
                make_statement(f"{final_2}", "*")
                print()

                # displays final equations in a simplified term matching form
                if display == final_1 == final_2:
                    print(f"This can additionally simplified to ({final_1})^3")
                elif display == final_1:
                    print(f"This can additionally simplified to ({display})^2({final_2})")
                elif display == final_2:
                    print(f"This can additionally simplified to ({display})^2({final_1})")
                elif final_1 == final_2:
                    print(f"This can additionally simplified to ({final_1})^2({display})")
                print()
                rr_raw.clear()
                rr_final.clear()
                rr_count.clear()
                questions_answered += 1




    """Finds and solves the equation for the quadratic"""
    # asks for the user input for their equation



# main routine goes here

make_statement("Cubic calculator", "-")
# instructions asker
instructions = yes_no("Do you want to read the instructions? ")
if instructions == "yes":
    show_instructions()

find_equation()


print()
print("Thank you for using the Cubic Calculator")