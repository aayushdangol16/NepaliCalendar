'''
nepali date --> done
day  ---> done
time ---> done
tithi(तिथि)
important event like (लोकतन्त्र दिवस , आमाको मुख हेर्ने दिन , 
हरितालिका तीज , संबिधान दिवस , फूलपाती, ग्याल्बो लोसार, विश्व पर्यटन दिवस , विश्व मजदुर दिवस) etc... 
when you give english date as input.
'''
from nepalicalendar import nepcalendar,BS
a=BS(2024,11,11)
print(a)

print(nepcalendar(2081,7))