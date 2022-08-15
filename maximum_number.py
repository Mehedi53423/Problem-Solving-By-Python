n1 = int(input("Enter The First Number : "))
n2 = int(input("Enter The Second Number : "))
n3 = int(input("Enter The Third Number : "))

if n1 > n2 and n1 > n3:
    print(n1, " Is The Maximum Number")
elif n2 > n1 and n2 > n3:
    print(n2, " Is The Maximum Number")
else: print(n3, " Is The Maximum Number")