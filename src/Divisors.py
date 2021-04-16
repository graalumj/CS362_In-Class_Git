#Divisor Calculator
#Alex Graalum
#CS 362
#4-15-2021
num = input("Enter number: ")
print("Divisors of " + str(num) + ": ")

for i in range(1, int(num/2)+1):
    if num % i == 0:
        print("- " + str(i))
