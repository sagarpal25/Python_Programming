number = int(input("Enter a number : "))
i = 1
sumEven = 0

while i <= number:
    if i % 2 == 0:
        sumEven += i
    i += 1

print("Sum of even numbers :", sumEven)  


