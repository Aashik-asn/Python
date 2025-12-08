n=int(input("Enter year to check whether it is Leap Yr or not: "))
if (n%4==0 and n%100!=0) or (n%400==0):
    print(f"{n} is a Leap year")
else:
    print(f"{n} is not a Leap year")
