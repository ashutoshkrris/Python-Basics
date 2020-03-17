import calendar,time

yy = int(input("Enter the year : "))
mm = int(input("Enter the month : "))

print("Displaying calendar : ")
time.sleep(2)
print(calendar.month(yy,mm))
