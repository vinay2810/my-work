year = int(input("enter year: "))
if (year%400==0 or ( year%4 == 0 and year%100!=0 )):
    print("It's a Leap year")
else:
    print("It's not a leap year")