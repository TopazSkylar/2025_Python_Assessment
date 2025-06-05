listy = []
listener = []
def find_factors(value):
    """Returns positive factors of a number (excluding 0)"""
    if value == 0:
        return [0]

    factors = []
    for f in range(1, abs(value) + 1):
        if value % f == 0:
            factors.append(f)
    return factors


def real_roots(a,d):
    fact_a = find_factors(a)
    fact_d = find_factors(d)
    for num1 in fact_d:
        for num2 in fact_a:
            roots = num1 / num2

            listy.append(roots)

    # one big list
    listy.sort()
    print(f"with dupes = {listy}")
    # removes dupes
    for i in listy:
        if i not in listener:
            listener.append(i)
    # final list
    print(f"final = {listener}")

a = -2
d = -4
real_roots(a,d)
