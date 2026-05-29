#in this code i will create a calculator that will perform basic operations in the terminal

def add(x, y):
    return x + y 

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        return "Error: division by zero is not allowed.  rsrs (; "
    
while True:
    print("\n\n----calculator----")
    symbol = input("Enter the operation you want to perform (+, -, *, /) or q to quit: ")
    if symbol == 'q':
        print("Goodbye!")
        break

    n1 = float(input("Enter the first number:"))
    n2 = float(input("Enter the second number:"))

    match symbol:
        case "+":
            print(f"{n1} + {n2} = {add(n1, n2)}")
        case "*":
            print(f"{n1} * {n2} = {multiply(n1, n2)}")     
        case "-":
            print(f"{n1} - {n2} = {subtract(n1, n2)}")
        case "/":
            print(f"{n1} / {n2} = {divide(n1, n2)}") 
        case _:
            print("Invalid operation")

    input("Enter to continue")             



        