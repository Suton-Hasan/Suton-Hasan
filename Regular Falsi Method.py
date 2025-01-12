MAX_ITER = 1000000
def func(x):
    return (x * x * x - x * x + 2)
def regulaFalsi(a, b):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b")
        return -1
    c = a
    for i in range(MAX_ITER):
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        if func(c) == 0:
            break
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
    print("The value of root is : ",c)
regulaFalsi(-200, 300)







