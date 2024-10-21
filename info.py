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

tithi_names = {
    1: "Pratipada",
    2: "Dwitiya",
    3: "Tritiya",
    4: "Chaturthi",
    5: "Panchami",
    6: "Shashthi",
    7: "Saptami",
    8: "Ashtami",
    9: "Navami",
    10: "Dashami",
    11: "Ekadashi",
    12: "Dwadashi",
    13: "Trayodashi",
    14: "Chaturdashi",
    15: "Purnima",
    16: "Pratipada",   
    17: "Dwitiya",     
    18: "Tritiya",     
    19: "Chaturthi",   
    20: "Panchami",   
    21: "Shashthi",   
    22: "Saptami",     
    23: "Ashtami",     
    24: "Navami",      
    25: "Dashami",     
    26: "Ekadashi",    
    27: "Dwadashi",    
    28: "Trayodashi",   
    29: "Chaturdashi",  
    30: "Amavasya"     
}

IMPORTANT_EVENTS = {
    (1, 1): "नयाँ वर्ष",  # Nepali New Year (BS)
    (1, 11): "लोकतन्त्र दिवस",  # Loktantra Diwas
    (1, 18): "विश्व मजदुर दिवस",  # International Labor Day
    (1, 30): "श्रीपञ्चमी",  # Shree Panchami
    (3, 8): "महिला दिवस",  # International Women's Day
    (5, 15): "कुशे औंशी",  # Kushe Aunshi
    (6, 3): "संबिधान दिवस",  # Constitution Day
    (6, 8): "विश्व वातावरण दिवस",  # World Environment Day
    (6, 11): "गणेश चतुर्थी",  # Ganesh Chaturthi
    (7, 1): "विश्व पर्यटन दिवस",  # World Tourism Day
    (9, 1): "विश्व पर्यटन दिवस",  # World Tourism Day
    (9, 7): "उधौली पर्व",  # Udhauli Parva
    (9, 12): "मोहनी नख",  # Mohani Nakha (Newa)
    (9, 15): "अन्नपूर्ण यात्रा",  # Annapurna Yatra
    (9, 23): "यमरी पुन्ही",  # Yomari Punhi
    (10, 1): "माघे संक्रान्ति",  # Maghe Sankranti
    (11, 7): "प्रजातन्त्र दिवस",  # Democracy Day

}