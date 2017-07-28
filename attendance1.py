#forif statement
#program to print the attendance of student

name = input("Enter the name of student:")
td = int(input("Enter the total days"))
att = int(input("Enter the number of days attended"))


if att < td:
    for i in range(1, td):
        num = (att / td) * 100

        if 100 > num >= 75:
            print(name, "attendance is", num, "not in defaulter list")
            break

        elif num >= 40:
            print(name, "attendance is", num, "in defaulter list")
            break
        else:
            print(name, "attendance is", num, "in detention list")
            break
else:
    print("kai pan chutiya kapu naka")