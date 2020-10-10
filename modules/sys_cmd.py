from i_o_engine import takeCommand
from i_o_engine import speak
import subprocess
import time
import os

bin_dir = os.path.join(os.path.normpath(os.path.dirname(__file__)), "bin")

def vlmChange():
    valid = False

    while not valid:
        speak('What volume sir, speak between 1 to 100.')
        volume = takeCommand()
        os.chdir(bin_dir)
        os.system("setvol beep " + volume)
        valid = True


def fullVolume():
    valid = False

    while not valid:
        os.chdir(bin_dir)
        os.system("setvol beep 100")
        speak("Volume set to full, sir!")
        valid = True


def mute():
    valid = False

    while not valid:
        os.chdir(bin_dir)
        speak("Muting Sir!")
        os.system("setvol mute")
        valid = True


def unmute():
    valid = False

    while not valid:
        os.chdir(bin_dir)
        os.system("setvol unmute")
        speak("Unmuted Sir!")
        valid = True


def shutdown():
    speak('Are you sure you want to shutdown your computer?')
    request1 = takeCommand()
    if 'yes' in request1:
        speak("Ok terminating processes, computer will shutdown now. Goodbye!")
        subprocess.call(["shutdown", "/s", "/t", "30"])
        time.sleep(7)
        exit()


def restart():
    speak('Are you sure you want to restart your computer?')
    request1 = takeCommand()
    if 'yes' in request1:
        speak('Ok fine sir, see you in a minute!')
        subprocess.call(["shutdown", "/r", "/t", "20"])
        time.sleep(7)
        exit()


def sleep():
    speak("Ok sir, see you soon, stay safe")
    path_to_sleep = os.path.dirname(__file__) + "/bin/sleep.bat"
    print(path_to_sleep)
    subprocess.Popen(path_to_sleep)