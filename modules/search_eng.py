from modules.i_o_engine import speak
import webbrowser
import time
# from selenium import webdriver
# import random


def search(query):
    address = 'http://www.google.com/#q='
    query = query.replace("search", "")
    speak('Ok sir, searching for' + query)
    newWord = address + query
    time.sleep(1.5)
    speak('Sir, results found!')
    webbrowser.open(newWord)


def openWebsite(website_name):
    webbrowser.open(website_name)

'''
def searchYoutube(query):
    address = 'https://www.youtube.com/results?search_query='
    query = query.replace("find videos on youtube for", "")
    speak('Ok sir, searching Youtube for' + query)
    newWord = address + query
    time.sleep(1)
    speak('Results Found!!')
    webbrowser.open(newWord)


def my_mix_shuffle():
    speak("Ok sir!")
    interested_bands = ['linkin park', 'imagine dragons']
    address = 'https://www.youtube.com/results?search_query='
    band_search = random.choice(interested_bands)
    main_add = address + band_search
    PATH = "C:\Program Files (x86)\msedgedriver.exe"
    driver = webdriver.Edge(PATH)
    driver.get(main_add)
    driver.maximize_window()
    speak("Here's Your music Sir!")
    play_music = driver.find_element_by_class_name("style-scope ytd-call-to-action-button-renderer")
    play_music.click()
'''