name = input("Enter the name of student:")
td = int(input("Enter the total days"))
att = int(input("Enter the attendance of student"))

if att >= 75:
    print(name,"attendance is",att,"not in defaulter list")

elif att >= 40:
    print(name, "attendance is", att, "in defaulter list")

else:
    print(name, "attendance is", att, "in detention list")
break
