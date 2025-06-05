factors_list = []
factors_list_2 = []
factors_list_3 = []
common_factors = []

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

def get_factors(to_factor, x, y, z):
    # list to hold factors

    if to_factor < 0:
        to_factor * -1

    limit = int(to_factor ** 0.5)


    # Find factor pairs and add to list
    if x == 1:
        for item in range(1, limit + 1):
                # Check if number is a factor
            result = to_factor % item
            factor_1 = int(to_factor // item)
            # Add factor to a list if it is not already there
            if result == 0:
                factors_list.append(factor_1)
                factors_list.append(-factor_1) # negative numbers are still factors
                if item not in factors_list:
                    factors_list.append(item)
                    factors_list.append(-item)

        factors_list.sort()
        common_factors.extend(factors_list)
        print(f"a factors {factors_list}")

    if y == 1: # Find factor pairs and add to list
        for item in range(1, limit + 1):
            # Check if number is a factor
            result = to_factor % item
            factor_1 = int(to_factor // item)
            # Add factor to a list if it is not already there
            if result == 0:
                factors_list_2.append(factor_1)
                factors_list_2.append(-factor_1) # negative numbers are still factors
                if item not in factors_list_2:
                    factors_list_2.append(item)
                    factors_list_2.append(-item)


        factors_list_2.sort()
        common_factors.extend(factors_list_2)
        print(f"b factors {factors_list_2}")


    if z == 1:
        # Find factor pairs and add to list
        for item in range(1, limit + 1):

            # Check if number is a factor
            result = to_factor % item
            factor_1 = int(to_factor // item)
            # Add factor to a list if it is not already there
            if result == 0:
                factors_list_3.append(factor_1)
                factors_list_3.append(-factor_1) # negative numbers are still factors
                if item not in factors_list_3:
                    factors_list_3.append(item)
                    factors_list_3.append(-item)

        factors_list_3.sort()
        common_factors.extend(factors_list_3)
        print(f"c factors {factors_list_3}")

        # find factors list
        common_factors.sort()
        print(f"common factors {common_factors}")
        neg_fact = min(set(factors_list) & set(factors_list_2) & set(factors_list_3))

        pos_fact = max(set(factors_list) & set(factors_list_2) & set(factors_list_3))


        print()
        print(f"Highest common factor {pos_fact}")
        print()
        print(f"Lowest common factor {neg_fact}")
        if a < 1:
            a2 = a/neg_fact
            b2 = b/neg_fact
            c2 = c/neg_fact

        else:
            a2 = a/int(pos_fact)
            b2 = b/int(pos_fact)
            c2 =c/int(pos_fact)

        print("--------------------------------")
        if neg_fact or pos_fact == -1 or 1:
            print("This is the simplest form your equation can be in")
            print(f"{a2}x^2+{b2}x+{c2}")
        else:
            print("Thus your equation simplifies to")
            print(f"{a2}x^2+{b2}x+{c2}")
        print()

def num_check(question):
    while True:

        try:
            response = float(input(question))
            return response

        except ValueError:
            print("Please enter a number")

while True:

    ask_a = "what is your a (x^2) value? "
    ask_b = "what is your b (x) value? "
    ask_c = "what is your c (constant) value? "

    a = num_check(ask_a)
    b = num_check(ask_b)
    c = num_check(ask_c)
    get_factors(a,1, 0, 0)
    get_factors(b,0,1,0)
    get_factors(c,0,0,1)



    # makes sure that the user wishes to solve the equation they just entered
    # (ERROR PREVENTION)
    confirmation = yes_no("Is this the equation you wish to solve?")
    print()
    if confirmation == "no":
        break
