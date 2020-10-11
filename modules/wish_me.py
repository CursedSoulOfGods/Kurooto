import datetime
from modules.i_o_engine import speak


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
    speak(f"Today is {date}, hope you are having a great day and will continue to have it")


def checkSpecialDays():
    check_month = int(datetime.datetime.now().month)
    check_day = int(datetime.datetime.now().day)
    if check_month == "your birth month" and check_day == "your birth date":
        speak("It's your birthday Sir!!! Happy Birthday, sorry I can't give you any presents, but it's been a great time working with you, thanks for making me so I can feel these moments for myself")
