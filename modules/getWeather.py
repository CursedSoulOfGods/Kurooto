from selenium import webdriver
from modules.i_o_engine import speak


def getWeather():
    PATH = "C:\Program Files (x86)\msedgedriver.exe"
    driver = webdriver.Edge(PATH)
    add = "https://weather.com/en-IN/weather/today/l/bdac7e9b00c8e927c0e20b6055cd4e4f38b0ecbdac85f53dc05b1e606065e962"
    speak("Hold on a minute sir, let me get the weather info for you")
    driver.get(add)
    driver.minimize_window()
    weather = driver.find_element_by_class_name("_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY").text
    condition = driver.find_element_by_class_name("_-_-components-src-organism-CurrentConditions-CurrentConditions--phraseValue--mZC_p").text
    try:
        prep_chance = driver.find_element_by_class_name("_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf").text
        driver.close()
        speak(f"Temperature right now is {weather} and it's {condition} outside. There are {prep_chance}")
    except Exception:
        driver.close()
        speak(f"Temperature right now is {weather} and it's {condition} outside.")