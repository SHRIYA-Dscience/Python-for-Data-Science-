# Find the Factorial of given number. 
num1 = int(input("Enter your number:"))
fact = 1
for i in range(1,num1+1):
    fact *= i
print("The factorial of give number is:",fact)