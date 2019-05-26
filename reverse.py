#print odd and even number
a = 50
while (a>0) :
    if(a%2==0):
        print("even" , a)
    else:
        print("odd" , a)
    a = a - 1

#infinite loop
#i=0
#while(i==0):
    #print("never ending loop")

#multiplication
a = int(input(" enter a number: "))
b = int(input(" enter a number: "))
result = 1
for x in range(a,b+1):
    result = x * result
print(" Result of multiplication is :", result)

#sum of n mumbers
a = int(input(" enter a lower range: "))
b = int(input(" enter a higher range: "))
sum = 0
for x in range (a,b+1):
    sum = sum + x
print("Sum of n numbers is :", sum)

#sum of even and odd
a = int(input(" enter a lower range: "))
b = int(input(" enter a higher range: "))
sum_even = 0
sum_odd = 0
for x in range (a,b+1):
    if (x % 2 == 0):
        sum_even = sum_even + x
    else:
        sum_odd = sum_odd + x
print("Sum of even numbers is :", sum_even)
print("Sum of odd numbers is :", sum_odd)

#sum of squares of even numbers:
a = int(input(" enter a lower range: "))
b = int(input(" enter a higher range: "))
sum = 0
for x in range (a,b+1):
    if (x % 2 == 0):
        sum = sum + x * x
    else:
        continue
print("Sum of square of even numbers is :", sum)

#sum of squares :
a = int(input(" enter a lower range: "))
b = int(input(" enter a higher range: "))
sum = 0
for x in range (a,b+1):
    for i in range (a,b+1):
        if (x /i == i):
            sum = sum + x
        else:
            continue
print("Sum of square is :", sum)




