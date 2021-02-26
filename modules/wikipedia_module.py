from i_o_engine import *
import wikipedia
#import webbrowser
#import time


def wikiSearch(query):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)

'''
def random_knowledge():
    page_to_be_provided = wikipedia.random(1)
    speak("Sir! Do you want to read about" + page_to_be_provided)
    print(page_to_be_provided)
    read_y_or_n = takeCommand()
    if 'yes' in read_y_or_n:
        load_page = wikipedia.page(page_to_be_provided)
        speak('Ok Sir! Here\'s the summary')
        print(load_page.summary)
        speak(load_page.summary)
        time.sleep(1)
        speak("Do you want me to open the article for you to read?")
        if_open = takeCommand()
        if 'yes' in if_open:
            webbrowser.open(load_page.url, new=2)
            speak("Here's the requested page Sir!")
        if 'no' in if_open:
            speak("Ok Sir!")
    if 'no' in read_y_or_n:
        speak("Ok Sir!")
'''