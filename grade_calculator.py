marks = int(input("Enter Your Marks : "))

if marks > 100 or marks < 0:
    print("Wrong Input! Please, Enter Your Marks. Which Is 1 to 100")
elif marks >= 80:
    print("Your Grade Is : A+")
elif marks >= 70:
    print("Your Grade Is : A")
elif marks >= 60:
    print("Your Grade Is : A-")
elif marks >= 50:
    print("Your Grade Is : B")
elif marks >= 40:
    print("Your Grade Is : C")
elif marks >= 33:
    print("Your Grade Is : D")
else: print("Your Grade Is : F")