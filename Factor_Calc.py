

def statement_generator(text, decoration):
    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


def num_check(question):
    valid = False
    while not valid:
        error = "Please enter an integer that is greater than or equal to one and less than or equal to 200"

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if 1 <= response <= 200:
                return response

            # Outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()

    # Main Routine

    statement_generator("Factors Calculator", "-")

    first_time_ = input("Press <enter> to see the instructions or any key to continue ")

    if first_time_ == "":
        instructions()


def instructions():
    statement_generator("Instructions/information", "-")
    print()
    print("Please choose a number than is greater than or equal to one and less than or equal to 200")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each "
          "calculation or any key to quit.")
    print()
    return ""


# Gets factors, returns a sorted list
def get_factors(to_factor):
    # list to hold factors
    factors_list = []

    # Square root factor to find 'half-way'
    limit = int(to_factor ** 0.5)

    # Find factor pairs and add to list
    for item in range(1, limit + 1):

        # Check if number is a factor
        result = to_factor % item
        factor_1 = int(to_factor // item)

        # Add factor to a list if it is not already there
        if result == 0:
            factors_list.append(factor_1)

            if item not in factors_list:
                factors_list.append(item)

        # if factor_1 != item and result == 0:
        #     factors_list.append(factor_1)

    # Output
    factors_list.sort()
    return factors_list


# Main routine goes here

# Heading
statement_generator("Factors Calculator", "-")

# Displays instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session

keep_going = ""
while keep_going == "":

    # initialise comment, this will be populated if the
    # number is a prime / perfect square
    comment = ""

    # ask user for a number to be factored
    var_to_factor = num_check("Number? ")

    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        comment = "One is Unity, it only has one factor that being itself"
        factor_list = ""

    # comments for squares / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)

    # if we have san odd number of factors, it's a perfect square
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)

    # output factors and comment

    # Generate heading
    if var_to_factor == 1:
        heading = "One is special. . ."

    else:
        heading = "Factors of {:.0f}".format(var_to_factor)

    # Output factors and comment
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thank you for using the factors calculator")
print()
