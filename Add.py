def addition(x,y):
    return(x+y)


def substraction(x, y):
    return(x-y)


def multiplication(x, y):
    return(x*y)


def Division(x, y):
    return(x/y)


print("Please select operation -\n" 
        "1. addition\n" 
        "2. substraction\n" 
        "3. multiplication\n" 
        "4. Division\n")

select = input("select an operation:")
n1 = int(input("enter a number :"))
n2 = int(input("enter a number :"))
if (select == "1"):
    print("Sum of numbers is :" , addition(n1,n2))
elif (select == "2"):
    print("Difference of numbers is :", substraction(n1,n2))
elif (select == "3"):
    print("Multiplication of numbers is :", multiplication(n1,n2))
elif (select == "4"):
    print("Division of numbers is :", Division(n1,n2))
else:
    print("Invalid Input")