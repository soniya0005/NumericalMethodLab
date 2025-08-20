opt = input("Enter an operator (+,-,*,/) : ")

n1 = int(input("Enter first numher : "))
n2 = int(input("Enter second number : "))

if opt == "+":
    print(f"Additon of {n1} + {n2} = {n1+n2}")
elif opt == "-":
    print(f"Subtraction of {n1} - {n2} = {n1-n2}")
elif opt == "*":
    print(f"Multiplication of {n1} * {n2} = {n1*n2}")
elif opt == "/":
    if n2 != 0:
        print(f"Division of {n1} / {n2} = {n1/n2:.2f}")
    else:
        print("Error! Division by zero")
else:
    print("Invalid operator")