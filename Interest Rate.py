from datetime import datetime
lab2="lab3:Interest Rate"
cname="cnet142:vidya rajasekaran-"
t=datetime.today().strftime("%b-%d-%y %a (%I:%M:%S %p)")
print(cname,end="")
print(lab2)
print(t)
print("\n")
while True:
    p = float(input("Enter the starting principal,0 to quit: "))
    if p>0:
        r=float(input("enter the annual interest rate: "))
        n=int(input("how many times per year is the interest compounded: "))
        t=float(input("for how many years will the account earn the interest: "))
        total = p * (1 + ( r / 100) / n) ** (n * t)
        interest = total -p
        print(f"At the end of {t} years you will have $ {total:.2f} with interest earned $ {interest:.2f}")
        print("\n")
    else:
        print("Program Exiting....")