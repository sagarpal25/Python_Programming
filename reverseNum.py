number = int(input("Enter a number : "))
ans = 0

while number > 0:
    digit = number%10
    ans = ans*10+digit
    number = number/10

print(ans)

#not solve
