def inefficientMultiplication(x, y):
    product = 0
    for i in range(x):
        product = product + y
    return product

if inefficientMultiplication(4, 5) == 20:
    print("Passed test 0")
else:
    print("Failed test 0")

def inefficientSquare(x):
    # this does not work on 0
    product = 1
    for i in range(2):
        product = product * x
    return product

if inefficientSquare(5) == 25:
    print("Passed test 1")
else:
    print("Failed test 1")