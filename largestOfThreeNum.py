firstNum = int(input("Enter first number: "))
secondNum = int(input("Enter second number: "))
thirdNum = int(input("Enter third number: "))

if firstNum >= secondNum and firstNum >= thirdNum:
    greatest = firstNum
elif secondNum >= firstNum and secondNum >= thirdNum:
    greatest = secondNum
else:
    greatest = secondNum

print("greatest number : ",greatest)