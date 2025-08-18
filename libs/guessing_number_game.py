import random 
print("*******This is our new game where guess the number then chekc with computer guess******")
low = int(input("Enter your starting number:"))
high = int(input("Enter your end number:"))

guess = random.randint(low,high)
ch = 5
for i in range(ch + 1):
    num = int(input("Enter your guess number:"))
    # gc += i 
    if num <= guess:
        print(num, "is to small")
    elif num > guess:
        print(num, "is high number")
    else:
        print(num," is match with",guess)
print("oops Yoour chances is finished. ")