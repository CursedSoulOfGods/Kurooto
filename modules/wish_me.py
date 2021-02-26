import datetime
from i_o_engine import speak
import os


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir!")

    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")


def getDate():
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().strftime("%H %M")
    speak(f"Today is {date} and it's {time}. Sir, I hope you are having a great day and will continue to have it")

'''
def checkSpecialDays():
    check_month = int(datetime.datetime.now().month)
    check_day = int(datetime.datetime.now().day)
    bday_store_loc = os.path.normpath(os.path.join((os.path.dirname(os.path.abspath(__file__))), "user\\user_info"))
    bday_store_loc = bday_store_loc.replace("\\modules", "")
    bd_file = open(bday_store_loc + "\\bday.KRT", 'r')
    birthday_date = bd_file.read()
    bd_file.close()

    birthday_date = birthday_date.split('-')
    birthday_date.pop(2)

    date = int(birthday_date[1])
    month = int(birthday_date[0])

    if check_month == month and check_day == date:
        speak("It's your birthday Sir!!! Happy Birthday, sorry I can't give you any presents, but it's been a great time working with you, thanks for making me so I can feel these moments for myself")
'''