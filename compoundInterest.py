principal = int(input("Enter the principal amount : "))
rate = int(input("Enter the annual rate of interest : "))
time = int (input("Enter the time : "))

amount = principal * (1 + rate/100) ** time
compoundInterest = amount - principal

print("Total Amount : ", amount)
print("Compound Interest : ", compoundInterest)