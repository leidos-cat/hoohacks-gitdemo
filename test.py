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

def inefficient_nth_power(x, n):
    """Raise a number (x) to the n-th power"""
    res = 1
    for i in range(n):
	    res = res * x
    return res

if inefficientSquare(5) == 25:
    print("Passed test 1")
else:
    print("Failed test 1")
    
if inefficient_nth_power(2, 3) == 8:
    print("Passed test 2")
else:
    print("Failed test 2")
