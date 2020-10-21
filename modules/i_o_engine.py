import pyttsx3
import speech_recognition as sr
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# input function
threshold_loc = os.path.normpath((os.path.join(os.path.dirname(__file__), "user/settings")))
threshold_loc = threshold_loc.replace("\\modules", "")
write_threshold = open(threshold_loc + "\\threshold.KRT", 'r')
threshold = write_threshold.read()
write_threshold.close()
threshold = int(threshold)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # display_text = "Listening"
        r.pause_threshold = 0.5
        r.energy_threshold = threshold
        audio = r.listen(source)
    try:
        print("Recognizing...")
        # display_text = "Recognizing"
        query = r.recognize_google(audio, language='en-en')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

# output system


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

takeCommand()