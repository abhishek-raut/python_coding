num = int(input("Enter the num"))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "it is not a prime number")
            print(i, "is a factor of", num)
            i += 1
        continue
        break
    else:
        print(num, "it is a prime number")