number  = int(input("Enter a digits : "))
ans = 0
while number > 0 : 
    digit = number % 10
    ans = ans + digit
    number = number/10

print("Sum : ",ans)
