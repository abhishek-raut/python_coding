#if else loop
#program for odd even sort

num = int(input("enter Number :"))

if num > 1:
    for i in range(num, 0, 2):
        if num % i == 0:
            print(num, "it is not a prime number")
            print(i, "is a factor of", num)
            break
    else:
        print(num, "is a prime number")


