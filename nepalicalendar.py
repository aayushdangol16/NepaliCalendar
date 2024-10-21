''' module that print the Nepali Calendar '''

from monthdays import check_monthDays
import calendar
from datetime import date

def BS(englishYear,englishMonth,englishDate):
    refEnglishYear=1944
    refEnglishMonth=1
    refEnglishDate=1
    day=calendar.SATURDAY

    refNepaliYear=2000
    refNepaliMonth=9
    refNepaliDate=17
    daycount=day

    ref_date=date(refEnglishYear,refEnglishMonth,refEnglishDate)
    provided_date=date(int(englishYear),int(englishMonth),int(englishDate))
    diff=(provided_date-ref_date).days

    NepaliYear=refNepaliYear
    NepaliMonth=refNepaliMonth
    NepaliDate=refNepaliDate

    while(diff!=0):
        daysinmonth=int(check_monthDays[NepaliYear][NepaliMonth-1])
        NepaliDate+=1

        if(NepaliDate>daysinmonth):
            NepaliMonth+=1
            NepaliDate=1
        if(NepaliMonth>12):
            NepaliYear+=1
            NepaliMonth=1

        daycount+=1
        if(daycount>6):
            daycount=0
        diff-=1
    return (f"{NepaliYear}-{NepaliMonth}-{NepaliDate} ({calendar.day_name[daycount]})")



def nepcalendar(year,month):
    day=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
    months = ["Baishakh","Jestha","Ashadh","Shrawan","Bhadra","Ashwin","Kartik","Mangsir","Poush","Magh","Falgun","Chaitra"]
    monthmap={
        1:4,
        2:5,
        3:6,
        4:7,
        5:8,
        6:9,
        7:10,
        8:11,
        9:12,
        10:1,
        11:2,
        12:3
    }
    daysinmonth=check_monthDays[year][month-1]
    admonth=monthmap[month]
    if admonth==1 or admonth==2 or admonth ==3:
        adyear=year-56
    else:
        adyear=year-57
    addate=27
    a=BS(adyear,admonth,addate)
    a=a.replace(" ","-").replace("(","").replace(")","").split("-")
    caldate=a[2]
    calday=a[3][:3]
    index=day.index(calday)
    x=int(caldate)
    while(x!=1):
        if index==0:
            index=6
        else:
            index-=1
        x-=1
    daylist=[]
    for i in range(0,index):
        daylist.append(" ")
    for i in range(1,int(daysinmonth)+1):
        daylist.append(str(i))
    #print(f"{months[month-1]} {year}".center(25))
    mainlist=[]
    headlist=[f"{months[month-1]} {year}".center(29)]
    headlist.append("\n")
    headdaylist=day

    mainlist.extend(headlist)
    mainlist.extend(headdaylist)
    bodylist=[]
    for i in range(0,len(daylist),7):
        # print(" ".join(str(x).center(3) for x in daylist[i:i+7]))
        bodylist.append("\n")
        bodylist.append(" ".join(str(x).center(3) for x in daylist[i:i+7]))

    mainlist.extend(bodylist)
    return(" ".join(mainlist))
