# importing modules
import site
import sys
import os
import random
module_path = os.path.dirname(__file__) + "\modules"
site.addsitedir(module_path)
site.addsitedir(module_path + "\sec")
site.addsitedir(module_path + "\cal")
from authn_prcess import *
from eml_prcess import *
from fl_wrtr import *
from search_eng import *
from sys_pow_cmds import *
from wish_me import *
from wikipedia import *
from google_cal_process import *
from getWeather import getWeather
from i_o_engine import *
# import serial

# Srl_send = serial.Serial('com6', 57600)
random.seed(time.process_time())
Srl_send = None

def relay1ON():
    speak("Turning on sir!!")
    Srl_send.write('1'.encode())
    time.sleep(1)


def relay1OFF():
    speak("Turning off sir!!")
    Srl_send.write('1'.encode())
    time.sleep(1)


def relay2ON():
    speak("Turning on sir!!")
    Srl_send.write('2'.encode())
    time.sleep(1)


def relay2OFF():
    speak("Turning off sir!!")
    Srl_send.write('2'.encode())
    time.sleep(1)


def relay3ON():
    speak("Turning on sir!!")
    Srl_send.write('3'.encode())

    time.sleep(1)


def relay3OFF():
    speak("Turning off sir!!")
    Srl_send.write('3'.encode())
    time.sleep(1)


def masterON():
    speak("Turning on all devices sir!!")
    Srl_send.write('1'.encode())
    time.sleep(1.5)
    Srl_send.write('2'.encode())
    time.sleep(1.5)
    Srl_send.write('3'.encode())
    time.sleep(1.5)


def masterOFF():
    speak("Turning off all devices sir!!")
    Srl_send.write('1'.encode())
    time.sleep(1.5)
    Srl_send.write('2'.encode())
    time.sleep(1.5)
    Srl_send.write('3'.encode())
    time.sleep(1.5)


# event trigger
if __name__ == "__main__":
    getCurrentLock()
    wishMe()
    getDate()
    # getWeather()
    checkSpecialDays()
    random_knowledge()
    # the whole commands
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            wikiSearch(query)

        elif 'open youtube' in query:
            openWebsite("youtube.com")

        elif 'open google' in query:
            openWebsite("google.com")

        elif 'open amazon' in query:
            openWebsite("amazon.in")

        elif 'open reddit' in query:
            openWebsite("reddit.com")

        # music
        elif 'play music' in query or 'I am getting bored' in query or 'play some tunes' in query:
            my_mix_shuffle()

        # time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        # emails
        elif 'email to my id' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sumangalam_avtar@yahoo.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry your majesty. I am not able to send this email")

        elif 'email to sarika' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sarikasharma259@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry your majesty. I am not able to send this email")

        elif 'email to siddharth' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "avtarbuilders1978@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry your majesty. I am not able to send this email")

        elif 'email to papa' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "avtarbuilders1978@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry your majesty. I am not able to send this email")

        elif 'write a file' in query:
            fileWrite()

        elif 'search' in query:
            search(query)

        elif 'find videos on youtube for' in query:
            searchYoutube(query)

        # normal conversations
        elif 'hi' in query or 'hello' in query:
            wishes1 = ['hi sir', 'yes sir', 'hello sir']
            speak(random.choice(wishes1))

        elif 'what are you doing' in query:
            boogo1 = ['trying to solve the mysteries of the universe',
                      'learning calculus at a higher level than einstien',
                      'solving mysteries of quantum gravity and fluctuations', 'listening to you sir']
            speak(random.choice(boogo1))

        elif 'crypto' in query or 'crew 2' in query or 'kukuruku' in query or 'kurooto' in query or 'guddu' in query or 'rto' in query:
            wishes = ['Yes my majesty', 'yes sir', 'attentive sir']
            speak(random.choice(wishes))

        elif 'thank you' in query:
            speak("Welcome your majesty")

        # exit commands
        elif 'quit' in query:
            speak('Goodbye Sir!')
            exit()

        elif 'bye' in query:
            speak('Goodbye Sir!')
            exit()

        elif 'goodbye' in query:
            speak('Goodbye Sir!')
            exit()

        # shutdown
        elif 'shutdown' in query or 'goodnight' in query or "good night" in query:
            shutdown()

        # restart
        elif 'restart' in query:
            restart()

        elif 'going off for some time' in query or 'will be coming back shortly' in query or 'see you after some time' in query:
            sleep()
        
        elif 'on' in query and 'first device' in query:
            relay1ON()

        elif 'off' in query and 'first device' in query or 'of' in query and 'first device' in query:
            relay1OFF()

        elif 'on' in query and 'second device' in query:
            relay2ON()

        elif 'off' in query and 'second device' in query or 'of' in query and 'second device' in query:
            relay2OFF()

        elif 'on' in query and 'last device' in query:
            relay3ON()

        elif 'off' in query and 'last device' in query or 'of' in query and 'last device' in query:
            relay3OFF()

        elif 'off' in query and 'all devices' in query or 'of' in query and 'all devices' in query:
            masterOFF()

        elif 'on' in query and 'all devices' in query:
            masterON()
        
        elif 'change volume' in query:
            vlm_change()

        elif 'mute' in query:
            mute()

        elif 'get my' and 'events' in query:
            n_events = 5
            service = get_cal_creds()
            get_events(n_events,service)
            print("Done")

        elif 'get my' and 'event' in query:
            n_events = 5
            service = get_cal_creds()
            get_events(n_events,service)
            print("Done")

        elif 'get my next' and 'event' in query:
            n_events = 1
            service = get_cal_creds()
            get_events(n_events,service)
            print("Done")

        elif 'what have I got on my calendar' in query:
            n_events = 5
            service = get_cal_creds()
            get_events(n_events,service)
            print("Done")

        elif 'what have I got to do right now' in query:
            n_events = 1
            service = get_cal_creds()
            get_events(n_events, service)
            print("Done")

        elif 'what is the weather now' in query or 'weather' in query:
            getWeather()