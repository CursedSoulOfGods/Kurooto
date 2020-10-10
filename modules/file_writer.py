from modules.i_o_engine import takeCommand
from modules.i_o_engine import speak
import os


base_dir = os.path.dirname(__file__).replace("modules/", "Files/")


def fileWrite():

    speak("What should I name the file as?")
    nameoffile = takeCommand()
    file = base_dir + nameoffile + ".txt"
    saveFile = open(file, 'w')
    speak("What should I write in the file?")
    towrite = takeCommand()
    speak("Are you sure you want to write this in the file?" + towrite)
    choicetowrite = takeCommand()
    if 'yes' in choicetowrite:
        saveFile.write(str(towrite))
        speak("File successfully written")
        saveFile.close()
    else:
        speak("Ok cancelling process.")
