def findMax(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

firstNum = int(input("Enter first number : "))
secondNum = int(input("Enter second number : "))
thirdNum = int(input("Enter third number : "))

print("Maximum number is : ", findMax(firstNum, secondNum, thirdNum))