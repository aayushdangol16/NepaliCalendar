import csv

def no_of_days(path):
    with open(path,"r") as file:
        month_data={}
        f=csv.reader(file)
        next(f)
        for data in f:
            year=int(data[0])
            months_day=data[1:]
            month_data[year]=months_day
    return(month_data)

path="calendar_bs.csv"
check_monthDays=no_of_days(path)
