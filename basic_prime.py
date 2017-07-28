num = int(input("Enter the number ;"))

num1 = num - 1
for i in range(2, num1):
    if num % i == 0:
        print(i, "is a factor of", num)
        print(num, "is not a prime number")
        break
    else:
        (num % i) != 0
        print(num, "is a prime number")
    break
