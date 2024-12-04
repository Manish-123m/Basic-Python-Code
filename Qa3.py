# ### ===   3.      Write a Python program that determines if a given year is a leap year or not. ================================================

year=int(input("Enter the Year "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"tHis {year} year is a leap year")
        else:
            print(f"this year {year} is not a leap year")
    else:
        print(f"This year {year} is leap a year")
else:
    print(f"THis year {year} is not leap a year")