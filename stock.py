stock = input("enter the items in stock")
check = input("enter the item you want")

if check in stock:
    print(check, "in stock")
else:
    print(check, "not in stock")