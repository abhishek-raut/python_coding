num = int(input("enter "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(i, "is a factor")
            print(num, "is not a prime number")
        continue

    else:
        print(num, "is a prime")