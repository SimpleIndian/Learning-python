# import a builtin module to import date funcanality
import datetime

x = datetime.datetime.now()  # get current time
print(x.minute)
print(x.strftime("%A"))  # print the weekday (full)

# creating date object --
getDate = datetime.datetime(2020, 5, 7)
# make in readable format
print(x.strftime("%B"))

# printing full date
getMonth = x.strftime("%B")
getYear = x.strftime("%Y")
getcurrentDate = x.strftime("%d")
print(getcurrentDate + "/" + getMonth + "/" + getYear)
