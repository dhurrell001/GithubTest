
def is_year_leap(year):
    return year % 4 == 0 and year % 100 !=0 or year % 400 ==0

def days_in_month(year, month):
    lMonths = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_year_leap and month == 2:
        return 29
    else: return lMonths[month-1]

def day_of_year(year, month, day):
    pass
    
print(day_of_year(2000, 12, 31))

#testing github
#=======
def is_year_leap(year):
    return year % 4 == 0 and year % 100 !=0 or year % 400 ==0

def days_in_month(year, month):
    lMonths = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_year_leap and month == 2:
        return 29
    else: return lMonths[month-1]

def day_of_year(year, month, day):
    pass
    
print(day_of_year(2000, 12, 31))

#This is seconnd test
