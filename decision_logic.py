# Prompt user for the tank's capacity in gallons
# Prompt user for miles_per_gallon
# Prompt user to enter gas price per gallon
# o MPG is less than 30: print out “It is not fuel efficient car.”
# o MPG is between 30 and 40, “It is average fuel efficient car.”
# o MPG is between 40 and 50, “It is fuel efficient car”
# o MPG is greater than 50, “It is very fuel efficient car”
"""Test case #1:
• capacity: 18.5
• miles per gallon: 33
• price per gallon: 3.89
Test case #2:
• capacity: 18.5
• miles per gallon: 45
• price per gallon: 3.89
Test case #3:
• capacity: 18.5
• miles per gallon: 60
• price per gallon: 3.89
 """
from datetime import datetime
lab2="lab2:car mileage"
cname="cnet142:vidya rajasekaran-"
t=datetime.today().strftime("%b-%d-%y %a (%I:%M:%S %p)")
print(cname,end="")
print(lab2)
print(t)
def func(t,c,p):
    cost=100/c*p
    distance=t*c
    print("Cost for driving 100 miles is:${:.2f}".format(cost))
    print("Distance on a tank of a gas is:{:.2f}".format(distance),"miles")
    if c<30:
        print(f"your car MPG is {c}.  It is not fuel efficient car.")
    elif (30<=c<=40):
        print(f"your car MPG is {c}.  It is average fuel efficient car.")
    elif 40 <= c <= 50:
        print(f"your car MPG is {c}.  It is fuel efficient car.")
    elif c>50:
        print(f"your car MPG is {c}.  It is very fuel efficient car.")
counter=0
while counter<3:
        print("case:",counter+1)
        t = float(input("enter the capacity of cars gas tank (in gallons):"))
        c = float(input("enter the cars miles per gallon:"))
        p = float(input("enter price per gallon:"))
        result = func(t, c, p)
        counter+=1






