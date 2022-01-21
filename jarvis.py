import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import pywhatkit
import webbrowser as wb
import os
from requests import get
import pyaudio
import urllib.request
from selenium import webdriver
from time import sleep

#pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #changing index changes voices
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Sorry i didn't catch that...")
        return ""
    print(repr(query))
    return query


def wish():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good after noon Sir!")
    elif hour >= 18 and hour < 24:
        speak("Good evening Sir!")
    else:
        speak("Hello sir")
    
    speak("I am jarvis your personal assistant")


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)



if __name__ == "__main__":
    wish()
    is_taking_commands = True
    while True:
        query = takeCommand()
        if 'go to sleep' in query.lower():
            speak("Goodbye Sir")
            is_taking_commands = False
        if 'activate' in query.lower():
            is_taking_commands = True
            speak("Online and ready sir")
        if not is_taking_commands:
            continue
        if 'according to wikipedia' in query.lower():
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=3)
                speak(results)
            except wikipedia.exceptions.PageError:
                pass

        elif 'what is your name' in query.lower():
            speak("My name is Jarvis, I am your personal assistant")

        elif 'open google' in query.lower():
            wb.open('https://google.com')

        elif 'open reddit' in query.lower():
            wb.open('https://reddit.com')

        elif 'open amazon' in query.lower():
            wb.open('https://amazon.ae')

        elif 'open wikipedia' in query.lower():
            wb.open('https://wikipedia.com')

        elif 'open discord' in query.lower():
            wb.open('https://discord.com/channels/@me')

        elif 'open gmail' in query.lower():
            wb.open('https://gmail.com')

        elif 'open yahoo' in query.lower():
            wb.open('https://yahoo.com')

        elif 'open twitter' in query.lower():
            wb.open('https://twitter.com')

        elif 'open stack overflow' in query.lower():
            wb.open('https://stackoverflow.com')

        elif 'what time is it' in query.lower():
            speak(time())

        elif 'what is the day' in query.lower():
            speak(date())

        elif 'search' in query.lower():
            search = query.replace('search', '')
            speak('searching ' + search)
            pywhatkit.search(search)

        elif "what is my ip" in query.lower():
            ip = get('https://api.ipify.org').text
            speak(f"your IP Address is {ip}")
            print(ip)

        elif 'thank you' in query.lower():
            speak("your welcome sir")

        elif 'shutdown' in query.lower():
            speak("Good bye sir")
            pywhatkit.shutdown(time=0)
        
        elif "youtube" in query.lower():
            ind = query.lower().split().index("youtube")
            search = query.split() [ind + 1:]
            wb.open(
                "https://www.youtube.com/results?search_query=" +
                "+".join(search)
            )

        elif "where is" in query.lower():
            ind = query.lower().split().index("is")
            location = query.split()[ind + 1:]
            url = "https://www.google.com/maps/place/" + "".join(location)
            wb.open(url)

        elif 'website' in query.lower():
            if query.startswith("website"):
                query = query[len('website'):].strip()
            wb.open(f"https://{query}.com")