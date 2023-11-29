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

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#start funzioni --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Buongiorno signore.")
  
    elif hour>=12 and hour<18:
        speak("Buon pomeriggio signore.")  
  
    else:
        speak("Buona sera signore.") 

def username():
    columns = shutil.get_terminal_size().columns
     
    print("########################".center(columns))
    print("\t\t\t\tWelcome to SamExe")  #uname.center(columns)
    print("########################".center(columns))
     
    speak("Come posso aiutarla?")

def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
        print("Sto ascoltando...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
        

        try:
            MyText = r.recognize_google(audio, language='it-IT')
            MyText = MyText.lower()
            if "oink" in MyText or "ink" in MyText or "link" in MyText:
                print("Sto ascoltando...")
                playsound("oink_boop.mp3")
                detect_command()
        except sr.UnknownValueError:
            print("Ascolto fallito.")

def your_Mic_Fuction():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Sto ascoltando...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language='it-IT')
            query = query.lower()
            print("Testo: " + query)
            your_query_Fuction(query)
            return query
        except Exception:
            print("Ascolto fallito")
            your_Mic_Fuction()

def your_query_Fuction(query):
    if "oink" in query or "ink" in query or "link" in query:
        playsound("oink_boop.mp3")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()

#end funzioni ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()
    #start ////////////////
    while True:
        
        query = your_Mic_Fuction()
        
        if "wikipedia" in query:
            speak("Sto cercando su wikipedia...")
            query = query.replace("wikipedia", "")
            print(query + "-->")
            results = wikipedia.summary(query, sentences = 3)
            speak("In accordo con Wikipedia:")
            print(results)
            speak(results)
 
        elif "apri youtube" in query:
            speak("Ecco a lei.\n")
            webbrowser.open("youtube.com")
 
        elif "apri google" in query:
            speak("Ecco a lei\n")
            webbrowser.open("google.com")
 
        elif 'apri classroom' in query:
            speak("Ecco a lei.")
            webbrowser.open("classroom.google.com")  
 
        elif "metti una canzone" in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "C:\\Users\\GAURAV\\Music"
            songs = os.listdir(music_dir)
            print(songs)   
            random = os.startfile(os.path.join(music_dir, songs[1]))
 
        elif query.startswith(("che ore sono", "orario", "dimmi che ore sono", "dimmi l'orario")):
            now = datetime.datetime.now()   # current time
            time = now.strftime('%H:%M')
            speak("sono le ore " + time)
##            strTime = datetime.datetime.now().strftime("% H:% M:% S")   
##            speak(f"Signore, sono le ore {strTime}")
 
        elif 'manda un email' in query:
            try:
                speak("Cosa devo dire?")
                content = your_Mic_Fuction()
                speak("Spedizione in corso")
                to = input()   
                sendEmail(to, content)
                speak("Email inviata.")
            except Exception as e:
                print(e)
                speak("Non è possibile inviare questa email.")
 
        elif "come ti chiami" in query or "qual è il tuo nome" in query:
            assname = "Samantha"
            speak("Sono ")
            speak(assname)
            print("Versione 0.0.1, ", assname)
 
        elif query.startswith(("stop", "Samantha stop", "spegniti", "samantha spegniti")):
            speak("Arrivederci signore")
            exit()
 
        elif "chi è il tuo creatore" in query or "chi ti ha creato" in query or "chi ti ha creata" in query:
            speak("Permessi riservati, non è possibile conoscere il mio creatore.")
             
##        elif "calcola" in query:
##            app_id = "KUTVQG-RXJ6JERH3W"
##            client = wolframalpha.Client(app_id)
##            indx = query.lower().split().index("calcola")
##            query = query.split()[indx + 1:]
##            res = client.query(' '.join(query))
##            answer = next(res.results).text
##            print("La soluzione è " + answer)
##            speak("La soluzione è " + answer)
 
        elif query.startswith(("cerca")):
            query = query.replace("cerca ", "")     
            webbrowser.open(query)
 
        elif "chi sono" in query:
            speak("La domanda è chi non è lei.")
 
##        elif 'news' in query:
##            try:
##                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
##                data = json.load(jsonObj)
##                i = 1
##                 
##                speak('here are some top news from the times of india')
##                print('''=============== TIMES OF INDIA ============'''+ '\n')
##                 
##                for item in data['articles']:
##                     
##                    print(str(i) + '. ' + item['title'] + '\n')
##                    print(item['description'] + '\n')
##                    speak(str(i) + '. ' + item['title'] + '\n')
##                    i += 1
##            except Exception as e:
##                 
##                print(str(e))
 
        elif "Arresta il sistema" in query:
                speak("Spegnimento in corso, arrivederci signore.")
                subprocess.call('shutdown / p /f')
 
        elif "non ascoltare" in query or "ferma l'ascolto" in query:
            speak("Per quanto tempo vuole fermare l'ascolto in secondi?")
            a = int(your_Mic_Fuction())
            time.sleep(a)
            print(a)
 
        elif query.startswith(("dov'è")):
            query = query.replace("dov'è ", "")
            location = query
            speak("Località")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif query.startswith(("dove si trova")):
            query = query.replace("dove si trova ", "")
            location = query
            speak("Località")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
 
        elif query.startswith(("fai una foto", "samantha fai una foto", "apri la camera", "apri la fotocamera")):
            ec.capture(0, "Samantha Camera ", "img.jpg")
 
        elif "riavvia" in query:
            subprocess.call(["shutdown", "/r"])
 
        elif query.startswith(("samantha scrivi una nota", "crea un file di testo", "samantha crea un file di testo", "samantha scrivi una nota", "scrivi un file di ")):
            speak("Cosa devo scrivere signore?")
            note = your_Mic_Fuction()
            file = open('SamText.txt', 'w')
            speak("Signore, devo includere anche data e ora?")
            snfm = takeCommand()
            if "si" in snfm or "certo" in snfm or "ovvio" in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "mostra file di testo" in query or "leggi quello che hai scritto" in query:
            speak("Lettura delle note:")
            file = open("SamText.txt", "r")
            print(file.read())
            speak(file.read(6))
 
        elif query.startswith(("meteo")):
             
            # Google Open weather website
            # to get API of Open weather
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak("Nome città:")
            print("Città: ")
            city_name = your_Mic_Fuction()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
             
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (kelvin) = " +str(current_temperature)+"\n Pressione atmosferica (hPa) ="+str(current_pressure) +"\n Umidità (%) = " +str(current_humidiy) +"\n Descrizione = " +str(weather_description))
             
            else:
                speak("Mi spiace signore, non sono riuscito a trovare la città.")
 
        elif query.startswith(("apri wikipedia")):
            webbrowser.open("wikipedia.com")
 
        # most asked question from google Assistant
        
 
        # elif "" in query:
            # Command go here
            # For adding more commands
    
