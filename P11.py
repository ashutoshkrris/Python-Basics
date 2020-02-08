year = int(input("Enter the year : "))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(str(year)+" is a leap year.")
        else:
            print(str(year)+" is not a leap year.")
    else:
        print(str(year)+" is a leap year.")
else:
    print(str(year)+" is not a leap year.")


'''                                     Output
                                Enter the year : 1900
                                1900 is not a leap year.

'''