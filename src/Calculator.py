#Simple Calculator
#Alex Graalum
#CS 362
#4-15-2021

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y
    
print("1) Add")
print("2) Subtract")
print("3) Multiply")
print("4) Divide")

while True:
    operate = input("Enter Operation: ")
    
    if operate in (1, 2, 3, 4):
        numA = float(input("Input 1: "))
        numB = float(input("Input 2: "))
        
        if operate == 1:
            string = str(numA) + " + " + str(numB) + " = " + str(add(numA, numB))
            print(string)
        if operate == 2:
            string = str(numA) + " - " + str(numB) + " = " + str(sub(numA, numB))
            print(string)
        if operate == 3:
            string = str(numA) + " * " + str(numB) + " = " + str(mul(numA, numB))
            print(string)
        if operate == 4:
            string = str(numA) + " / " + str(numB) + " = " + str(div(numA, numB))
            print(string)
        break

    else:
        print("ERROR: Input not valid")
