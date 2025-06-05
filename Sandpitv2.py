# # factors
# a = [1]
# b = [2]
# c = [1]
# # compilation all onto a single list
# d = a + b + c
# # what list will display
# print(d)
# # highest common factor of the lists
# g = max(set(a) & set(b) & set(c))
# if g == ValueError:
#     print("uh oh")

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

thingy = get_factors(5)
print(thingy)
