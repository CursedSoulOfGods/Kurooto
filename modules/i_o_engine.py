import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# input function


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # display_text = "Listening"
        r.pause_threshold = 0.5
        r.energy_threshold = 3500
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
