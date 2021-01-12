while True:
    equation = input("Enter your equation here:\n").replace('=', '==')
    for x in range(-1, 10):
        try:
            if eval(equation.format(*[x] * 2)) == True:
                print(x)
                print(f"{equation.format(*[x] * 2)}")
        except:
            pass