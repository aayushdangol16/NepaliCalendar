''' module that print the Nepali Calendar '''

from info import check_monthDays,IMPORTANT_EVENTS,tithi_names
import calendar
from datetime import date,datetime
import requests
import ephem

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
    return ([f"{NepaliYear}-{NepaliMonth}-{NepaliDate}",f"{calendar.day_name[daycount]}"])

def event(year,month,date):
    a=BS(year,month,date)[0]
    a=a.split("-")
    month=int(a[1])
    date=int(a[2])
    a=(month,date)
    if(a in IMPORTANT_EVENTS):
        return(IMPORTANT_EVENTS[a])
    else:
        return("No event")



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
    b=a[0].split("-")
    caldate=b[2]
    calday=a[1][:3]
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


def time():
    now = datetime.now()
    time_12hr = now.strftime("%I:%M %p")
    return time_12hr

def get_current_location():
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        location = data['loc'].split(',')
        latitude, longitude = location[0], location[1]
        return latitude, longitude
    except Exception as e:
        raise ValueError("Could not determine location: " + str(e))
    
def tithi(date_in):
    latitude, longitude = get_current_location()

    
    observer = ephem.Observer()
    observer.lat = latitude  
    observer.lon = longitude  
    
    date_in = ephem.Date(date_in)  
    observer.date = date_in

    # Get solar longitude
    sun = ephem.Sun(observer)
    solar_longitude = sun.hlon  

    # Get lunar longitude
    moon = ephem.Moon(observer)
    lunar_longitude = moon.hlon  

    
    new_moon = ephem.previous_new_moon(observer.date)

    
    lunar_age = observer.date - new_moon  

    
    tithi = int(lunar_age * 30 / 29.53) + 1  

    
    paksha = "Shukla Paksha" if tithi <= 15 else "Krishna Paksha"

    return f"{tithi_names[tithi]},{paksha}"

def nepali(year,month,dates):
    result={}
    bs=BS(year,month,dates)
    result['date']=bs[0]
    result['day']=bs[1]
    result['time']=time()
    result['tithi']=tithi(date(year,month,dates))
    e=event(year,month,dates)
    result['event']=e
    return(result)

