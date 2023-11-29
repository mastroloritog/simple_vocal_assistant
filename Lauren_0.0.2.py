import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
#from client.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from google_trans_new import google_translator
from googletrans import Translator, constants
from pprint import pprint

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#start funzioni --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Buongiorno signore.")
  
    elif hour>=12 and hour<18:
        speak("Buon pomeriggio signore.")  
  
    else:
        speak("Buona sera signore.")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Sto ascoltando...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio, language='it-IT')
            print(f"Testo: {statement}\n")

        except Exception as e:
            #speak("Mi scusi, si è riscontrato un errore nell'ascolto")
            return "None"
        
        return statement

#end funzioni ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#print("")
#speak("")
wishMe()

if __name__ == '__main__':
    speak("Come posso aiutarla?")
    while True:
        statement = takeCommand().lower()
        
        if statement==0:
            continue
        elif statement.startswith(("stop", "lauren stop", "spegniti", "lauren spegniti")):
            speak("Arrivederci signore")
            exit()
        elif "wikipedia" in statement:
            #print(wikipedia.suggest("Physics"))
            #print(wikipedia.search("Physics", results=1))

            try:
                translator = Translator()
                statement = statement.replace("wikipedia", "")
                statement = translator.translate(statement, lang_src='it', lang_tgt='en')
                print("Argomenti trovati per " + statement.text + ": ")
                speak("Argomenti trovati per " + statement.text + ": ")
                print(wikipedia.search(statement.text))
                speak(wikipedia.search(statement.text))
                print("Quale le interessa?")
                speak("Quale le interessa?")
                argumentWiki = takeCommand()
            except:
                speak("Mi scusi, non sono state trovate informazioni riguardo questo argomento")

            try:
                print(argumentWiki + "--> ")
                results = wikipedia.summary(argumentWiki, sentences = 3)
                results = results.split(".")
                speak("In accordo con Wikipedia: ")
                for phrase in results:
                    wikiText = translator.translate(phrase, lang_src='en', lang_tgt='it')
                    print(wikiText.text)
                    speak(wikiText.text)
            except:
                speak("Mi scusi, si è riscontrato un errore durante la ricerca Wiki")
        elif "apri google" in statement:
            speak("Ecco a lei\n")
            webbrowser.open("google.com")
        elif "apri youtube" in statement:
            speak("Ecco a lei.\n")
            webbrowser.open("youtube.com")
        elif 'apri classroom' in statement:
            speak("Ecco a lei.")
            webbrowser.open("classroom.google.com")
        elif statement.startswith(("apri wikipedia")):
            webbrowser.open("wikipedia.com")
        elif statement.startswith(("che ore sono", "orario", "dimmi che ore sono", "dimmi l'orario", "lauren che ore sono", "lauren dimmi l'orario")):
            now = datetime.datetime.now()   # current time
            time = now.strftime('%H:%M')
            speak("sono le ore " + time)
##            strTime = datetime.datetime.now().strftime("% H:% M:% S")   
##            speak(f"Signore, sono le ore {strTime}")
        elif "come ti chiami" in statement or "qual è il tuo nome" in statement:
            assname = "Lauren"
            speak("Sono ")
            speak(assname)
            print("Versione 0.0.2, ", assname)
        elif "chi è il tuo creatore" in statement or "chi ti ha creato" in statement or "chi ti ha creata" in statement:
            speak("Permessi riservati, non è possibile conoscere il mio creatore.")
        elif statement.startswith(("cerca", "lauren cerca")):
            statement = statement.replace("cerca ", "")     
            webbrowser.open(query)
        elif statement.startswith(("Arresta il sistema", "lauren arresta il sistema", "spegni il computer", "lauren spegni il computer")):
            speak("Spegnimento in corso, arrivederci signore.")
            subprocess.call('shutdown / p /f')
        elif "riavvia" in statement:
            subprocess.call(["shutdown", "/r"])
        elif "non ascoltare per" in statement or "ferma l'ascolto" in statement or statement.startswith("stop ascolto") or "lauren non ascoltare per" in statement:
            speak("Per quanti secondi vuole fermare l'ascolto?")
            a = takeCommand()
            print(a)
            a = a.split(" ")
            try:
                speak("A tra poco, signore")
                time.sleep(int(a[0]))
                speak("Stop ascolto terminato")
            except:
                speak("Mi dispiace, si è riscontrato un errore nello stop ascolto.")
