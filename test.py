def inefficientMultiplication(x, y):
    product = 0
    for i in range(x):
        product = product + y
    return product

if inefficientMultiplication(4, 5) == 20:
    print("Passed test 0")
else:
    print("Failed test 0")

#if inefficientSquare(5) == 25:
#    print("Passed test 1")
#else:
#    print("Failed test 1")