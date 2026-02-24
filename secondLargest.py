numbers = []

print("Enter 10 numbers :")
for i in range(10):
    num = int(input())
    numbers.append(num)

for num in numbers:
    print(num)





for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest number is:", second)






# numbers = list(map(int, input("Enter 10 numbers: ").split()))

# for num in numbers:
#     print(num)





#Not solve this questions