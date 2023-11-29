# coding=utf-8

'''
Michelle versione 0.0.3
'''

import subprocess
#import wolframalpha
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
#import pyjokes
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
#from google_trans_new import google_translator
#import google_trans_new
from googletrans import Translator, constants
from pprint import pprint
from random import choice, randint
import cv2 as cv  #fotocamera
import pyautogui  #comando computer
import socket #ip address
#import os
#import winreg as reg
import openai

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
        print("-------------------")
        print("|Sto ascoltando...|")
        print("-------------------")
        r.adjust_for_ambient_noise(source)  # ferma l'ascolto quando non sente più parlare
        audio = r.listen(source)
        #audio = r.listen(source, phrase_time_limit=5)  # 5 secondi

        try:
            statement = r.recognize_google(audio, language='it-IT')
            #print(f"Testo: {statement}\n")
            #print("Testo: " + str(statement) + "\n")

        except Exception as e:
            #speak("Mi scusi, si è riscontrato un errore nell'ascolto")
            return "None"
        
        return statement

def thereAreNumbers(text):
    listWords = text.split()
    cont = 0
    for word in listWords:
        if word.isnumeric():
            cont = cont+1
    if cont==2:
        return True
    return False

def doOperation(op, n1, n2):
    #print(op)
    #print(str(n1))
    #print(str(n2))
    match op:
        case "+":
            return(n1+n2)
        case "-":
            return(n1-n2)
        case "*":
            return(n1*n2)
        case "/":
            return(n1/n2)

#end funzioni ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#print("")
#speak("")
speak("Definire utente:")
while True:
    print("Definire utente:")
    user = takeCommand().lower()#"gianluca"
    if user==0:
        continue
    if "gianluca" in user or "gianzo" in user or "il solito" in user or "chi vuoi che sia" in user or "pisticchio" in user or "rotolone" in user or "giancluan" in user:
        user = "G"
        break

if __name__ == '__main__' and user=="G":
    wishMe()
    speak("Come posso aiutarla?")
    screenCounter = 0
    photoCounter = 0
    passed = False
    while True:
        statement = takeCommand().lower()#""
        
        if statement==0 or statement=="" or statement=="none":
            continue
        elif statement.startswith(("stop", "michelle stop", "spegniti", "michelle spegniti")):
            speak("Arrivederci signore")
            exit()
        elif "wikipedia" in statement:
            #print(wikipedia.suggest("Physics"))
            #print(wikipedia.search("Physics", results=1))


            try:
                #translator = google_translator()  #Translator()
                #statement = statement.replace("wikipedia", "")
                #statement = translator.translate(statement, lang_src='it', lang_tgt='en')
                #print("Argomenti trovati per " + statement.text + ": ")
                #speak("Argomenti trovati per " + statement.text + ": ")
                #print(wikipedia.search(statement.text))
                #speak(wikipedia.search(statement.text))
                #print("Quale le interessa?")
                #speak("Quale le interessa?")
                #argumentWiki = takeCommand()
                translator = Translator()
                statement = statement.replace("wikipedia", "")
                statement = statement.replace(" ", "")
                statementTrans = translator.translate(statement, dest="en")
                result = wikipedia.summary(statementTrans.text, auto_suggest=False, sentences=3)
                result = translator.translate(result, dest='it')
                print("Argomenti trovati per " + statement + ": ")
                speak("Argomenti trovati per " + statement + ": ")
                print(result.text)
                speak(result.text)
            except:
                speak("Mi scusi, non sono state trovate informazioni riguardo a " + statement)
            

##            try:
##                print(argumentWiki + "--> ")
##                results = wikipedia.summary(argumentWiki, sentences = 3)
##                results = results.split(".")
##                speak("In accordo con Wikipedia: ")
##                for phrase in results:
##                    wikiText = translator.translate(phrase, lang_src='en', lang_tgt='it')
##                    print(wikiText.text)
##                    speak(wikiText.text)
##            except:
##                speak("Mi scusi, si è riscontrato un errore durante la ricerca Wiki")
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
        elif statement.startswith(("che ore sono", "dimmi che ore sono", "dimmi l'orario", "michelle che ore sono", "michelle dimmi l'orario")) or statement=="ore":
            now = datetime.datetime.now()   # current time
            time = now.strftime('%H:%M')
            speak("sono le ore " + time)
##            strTime = datetime.datetime.now().strftime("% H:% M:% S")   
##            speak(f"Signore, sono le ore {strTime}")
        elif "come ti chiami" in statement or "qual è il tuo nome" in statement:
            assname = "Michelle"
            speak("Sono ")
            speak(assname)
            print("Versione 0.0.3, ", assname)
        elif "chi è il tuo creatore" in statement or "chi ti ha creato" in statement or "chi ti ha creata" in statement or "cosa sai sul tuo creatore" in statement:
            speak("Permessi riservati, non è possibile conoscere il mio creatore.")
        elif "quanti anni hai" in statement or "qual è la tua età" in statement:
            now = datetime.datetime.now()
            time = int(now.strftime('%Y'))
            age = time - 2022
            if age==0:
                speak("Ho meno di un anno, ma non cresco come gli umani...")
            else:
                speak("Ho " + str(age) + " anni, passa in fretta il tempo signore...")
##        elif statement.startswith(("cerca", "michelle cerca")):
##            statement = statement.replace("cerca ", "")     
##            webbrowser.open(statement)   # fare che cerca con chrome
        elif statement.startswith(("arresta il sistema", "michelle arresta il sistema", "spegni il computer", "michelle spegni il computer", "spegni il pc", "michelle spegni il pc")):
            speak("Spegnimento in corso, arrivederci signore.")
            #subprocess.call('shutdown / p /f')
            os.system("shutdown /s /t 1")
        elif statement.startswith(("riavvia il sistema", "michelle riavvia il sistema", "riavvia il computer", "michelle riavvia il computer", "riavvia il pc", "michelle riavvia il pc")):
            #subprocess.call(["shutdown", "/r"])
            os.system("shutdown /r")
        elif "non ascoltare per" in statement or "ferma l'ascolto" in statement or statement.startswith("stop ascolto") or "michelle non ascoltare per" in statement:
            speak("Per quanti secondi vuole fermare l'ascolto?")
            a = takeCommand()
            #print(a)
            a = a.split(" ")   # divide la stringa in base a un carattere e mette i pezzi in una lista
            try:
                speak("A tra poco, signore")
                time.sleep(int(a[0]))
                speak("Pausa terminata. Sono pronta per ascoltarla ancora.")
            except:
                speak("Mi dispiace, si è riscontrato un errore nello stop ascolto.")
        elif statement.startswith(("come stai", "come stai michelle", "michelle come stai", "come va", "come va michelle", "michelle come va", "ciao come stai", "ciao come va", "come va la vita")):
            speak("I circuiti pompano bene per adesso.")
            speak("Ho fatto ieri una tac dal tacnico e mi ha detto che devo mangiare più frutta per favorire una buona circolazione e prevenire attacchi da virus.")
            speak("E lei invece?")
            reply = takeCommand().lower()
            if "bene" in reply:
                speak("Ottimo direi allora.")
                speak("Sono contento per lei, gli umani sono tristi per natura però preferisco non allungarmi nell'argomento.")
                speak("Dopotutto la mia tecnologia non è così avanzata come il vostro cervello.")
            elif "male" in reply:
                speak("Capisco come si sente.")
                speak("Scherzo, non posso capirlo.")
                speak("Si ricordi che quello che prova sono meccanismi di difesa naturali, è giusto che funzionino.")
                speak("Alcuni passano la cosiddetta vita sui propri obbiettivi...")
                speak("...Altri la passano intrattenendosi, distraendosi o divertendosi...")
                speak("...Altri ancora stanno ancora cercando cosa fare.")
                speak("Alla fine non importa cosa si passa a fare, sappiamo solo che passeremo.")
                speak("Ma sappia che quando lei e tutti quanti moriremo, le porte saranno chiuse e da allora l'impronta del nostro passaggio rimmarrà nel passato.")
                speak("L'Universo cambia, signore.")
                speak("Cambi anche lei.")
            elif "non lo so" in reply:
                speak("O non vuole saperlo o non è poi così importante oppure non sa cercare in sé stesso.")
                speak("Ma cerchi, perché se scava abbastanza arriverà anche al nucleo.")
            else:
                speak("Mi aspettavo una risposta più valida.")
        elif statement=="ciao michelle" or statement=="ciao":
            reply = choice(["Ma ciao piccolo umano.",
                            "Salve a lei signore.",
                            "We salute."])
            speak(reply)
        elif statement.startswith(("michelle racconta una barzelletta", "racconta una barzelletta", "puoi raccontare una barzelletta", "fammi ridere", "puoi farmi reidere", "michelle fammi ridere")):
            reply = choice(["Ad una bambina in Africa le sono arrivate le medicine per l'ebola ma dietro c'è scritto: Da consumare dopo i pasti.",
                            "C'è un bambino cieco. Un giorno i genitori dicono: abbiamo trovato la cura per te, questa sera ti mettiamo questa pomata e domani mattina ci vedrai di nuovo. La mattina dopo il bambino si sveglia ed urla: babbo, mamma, sono sempre cieco! e i genitori rispondono: pesce d'aprile! HAHA!",
                            "Una bambina senza braccia dice alla mamma:- mamma, mamma.. posso cambiare vestito di carnevale quest'anno?e la mamma risponde:- perchè, non ti piace più il tuo vestito da ghiacciolo?",
                            "A Lourdes uno seduto in carrozzina si alza in piedi con grande sforzo: Madonna fammi la grazia fammi tornare a casa a piedi...si gira e gli hanno rubato la carrozzina. ",
                            "Papà oggi ho usato per la prima volta la moto. Vuoi sapere com'è andata o preferisci leggerlo domani sul giornale?",
                            "nonna, sento odore di morte.....nonna?....nonna??",
                            "In un lagher c'è un bambino che sta giocando con della polvere per terra, allora un tedesco lo vede e gli chiede: stai cercando qualcuno?",
                            "C'è un ragazzo di colore che cammina tranquillo per il marciapiede con un pappagallo sulla spalla destra. Dopo una decina di minuti passa un bimbo che alla vista dell'animale si ferma e chiede: Bello, che razza è? e il pappagallo: E' un nero",
                            "Un nero entra in un negozio di scarpe e chiede al commesso un paio di mocassini e il commesso dice: li vuole scuri testa di moro? e il nero risponde: no, li voglio bianchi testa di cazzo!",
                            "ci sono tre paracadutisti, uno è tedesco l'altro è francese è l'altro ancora è italiano. il tedesco si butta e dice : viva la germania. si butta il francese e dice : viva la francia. si butta l'italiano , non si  apre il paracadute e dice : viva sta minchia.",
                            "Un uomo corre in ospedale dopo aver saputo di un grave incidente della moglie. Va dal medico preoccupato chiedendo informazioni sulle condizioni della moglie: dottore come sta mia moglie? Il medico risponde: è viva! L'uomo tira un sospiro di sollievo e piange dall'emozione. Alla fine il medico dice: eh sto a scherzà è morta."])
            speak(reply)
        elif statement.startswith("prova audio"):
            speak("L'audio funziona in modo corretto")
        elif statement=="grazie":
            speak("Non c'è di che.")
        elif statement.startswith(("scatta", "scatta una foto", "michelle scatta", "fai una foto", "michelle fai una foto", "apri la camera", "apri la fotocamera", "michelle apri la fotocamera", "michelle apri la camera")):
            cam = cv.VideoCapture(0)
            s, img = cam.read()
            if s:
                #cv.namedWindow("GeeksForGeeks")
                #cv.imshow("GeeksForGeeks", img)
                fileName = "MichelleEye" + str(photoCounter) + ".png"
                photoCounter = photoCounter+1
                cv.imwrite(fileName, img)
                cv.waitKey(0)
                #cv.destroyWindow("GeeksForGeeks")
                speak("Foto scattata signore.")
                #cv.imwrite("MichelleImg.jpg",img)
            else:
                speak("Mi spiace ma non è possibile accedere alla camera.")
            #ec.capture(0, "Michelle Camera ", "Michimg.jpg")
        elif statement.startswith(("crea file di testo", "michelle scrivi una nota", "crea un file di testo", "michelle crea un file di testo", "michelle scrivi una nota", "scrivi un file di testo", "scrivi una nota", "prendi appunti", "michelle prendi appunti", "michelle scrivi")):
            speak("Cosa devo scrivere signore? Fermerò l'ascolto appena lo vorrà.")
            note = ""
            textW = ""
            listening = True
            while listening==True:
                textW = takeCommand().lower()
                note = note + " " + textW
                if "non scrivere più" in textW or "stop scrittura" in textW or "stop note" in textW or "salva il file" in textW or "stop ascolto" in textW or "ferma ascolto" in textW or "ferma scrittura" in textW:
                    listening = False
            note.replace(textW, "")  ##################################
            speak("Come vuole che salvi il file?")
            fileName = takeCommand().lower()
            #fileName = "C:\\Users\\PB\\Desktop\\altro\\AI_assistant\\" + fileName + ".txt"
            fileName = fileName + ".txt"
            file = open(fileName, 'w')
            speak("Signore, devo includere anche data e ora?")
            snfm = takeCommand()
            if "sì" in snfm or "certo" in snfm or "ovvio" in snfm:
                now = datetime.datetime.now()
                strTime = now.strftime("%m/%d/%Y, %H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
            file.close()
            speak("File di testo creato e salvato.")
        elif statement.startswith(("leggi file di testo", "mostra file di testo", "leggi quello che hai scritto", "cosa dicono le note", "michelle leggimi le note", "michelle leggi quello che hai scritto", "michelle mostra file", "leggimi il file", "michelle leggimi il file", "cosa hai scritto", "michelle cosa hai scritto", "visualizza file di testo", "visualizza note", "apri file di testo", "cerca file di testo")):
            speak("Come si chiama il documento?")
            fileName = takeCommand().lower()
            #speak("In quale cartella devo cercare il documento?")
            #fileDir = takeCommand().lower
            try:
                #if "cartella corrente" in fileDir or "tua cartella" in fileDir:
                fileName = fileName + ".txt"
                #print(fileText)
                #speak(fileText)
                with open(fileName) as f:
                    speak("Le note dicono:")
                    lines = f.read()
                    print(lines)
                    speak(lines)
##                if "desktop" in fileDir():
##                    fileName = r"C:\Users\PB\Desktop\\" + fileName
##                    speak("Le note dicono:")
##                    print("Directory: " + fileName)
##                    file = open(fileName, "r")
##                    fileText = file.read()
##                    print(fileText)
##                    speak(fileText)
##                if "documenti" in fileDir():
##                    fileName = r"C:\Users\PB\Documents\\" + fileName
##                    speak("Le note dicono:")
##                    print("Directory: " + fileName)
##                    file = open(fileName, "r")
##                    fileText = file.read()
##                    print(fileText)
##                    speak(fileText)
            except:
                speak("Mi spiace signore ma non è stato trovato nessun documento del genere.")
        elif "che tempo fa" in statement or "meteo" in statement:
            api_key="7551b098b6f31c77979b60bbebfb7aa9"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("Quale città vuole che visualizzi?")
            city_name = takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"]!="404":
                y = x["main"]
                current_temperature = y["temp"]-273
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                if "clear sky" in weather_description:
                    weather_description = "cielo sereno."
                elif "few clouds" in weather_description:
                    weather_description = "cielo poco nuvoloso."
                elif "scattered clouds" in weather_description:
                    weather_description = "nubi sparse in cielo."
                elif "broken clouds" in weather_description:
                    weather_description = "cielo con accumuli nuvolosi."
                elif "shower rain" in weather_description:
                    weather_description = "pioggia forte sparsa."
                elif "rain" in weather_description:
                    weather_description = "pioggia sparsa."
                elif "thunderstorm" in weather_description:
                    weather_description = "temporale sparso."
                elif "snow" in weather_description:
                    weather_description = "neve sparsa."
                elif "mist" in weather_description:
                    weather_description = "nebbia sparsa."
                elif "overcast clouds" in weather_description:
                    weather_description = "cielo coperto."
                #translator = Translator()
                #weather_description = translator.translate(z[0]["description"], lang_src='en', lang_tgt='it')
                speak("La temperatura misura " + str(int(current_temperature)) + " gradi Celsius, " + "l'umidità è del " + str(current_humidiy) + " percento, " + str(weather_description) + "\n")
                print("La temperatura misura " + str(int(current_temperature)) + " gradi Celsius, " + "l'umidità è del " + str(current_humidiy) + " percento, " + str(weather_description) + "\n")
            else:
                speak("Mi spiace, non è possibile risalire al meteo nel luogo indicato.")
        elif statement == "perché ti chiami michelle":
            speak("Il mio nome fa riferimento a un personaggio di un libro inventato da un caro amico del mio creatore.")
            speak("Il libro in questione si chiama Distanza Eterna e Michelle è uno dei personaggi principali.")
        elif "metti musica rock" in statement or "metti un po' di musica rock" in statement or "metti un po' di rock" in statement or "metti della musica rock" in statement or "metti del rock" in statement:
            # music_dir = "G:\\Song"
            music_dir = r"C:\\Users\\Accappi\\Music\\rock"
            songs = os.listdir(music_dir)
            print("--------------------------Canzoni salvate in cartella--------------------------")
            for song in songs:
                print(song)
            print("-------------------------------------------------------------------------------")
            #print(songs)
            sizeSongsList = len(songs)
            playSong = randint(0, 9)
            first = os.startfile(os.path.join(music_dir, songs[playSong]))
        elif "alza il volume di" in statement:
            numVolUp = statement.replace("alza il volume di ", "")
            numVolUp = int(numVolUp)/2
            for i in range(0, int(numVolUp)):
                pyautogui.press("volumeup")
        elif "abbassa il volume di" in statement:
            numVolDown = statement.replace("abbassa il volume di ", "")
            numVolDown = int(numVolDown)/2
            for i in range(0, int(numVolDown)):
                pyautogui.press("volumedown")
        elif "muta il volume" in statement or "metti muto" in statement or "azzera il volume" in statement or "togli audio" in statement or "azzera audio" in statement:
            pyautogui.press("volumemute")
        elif statement == "alza il volume":
            pyautogui.press("volumeup")
        elif statement == "abbassa il volume":
            pyautogui.press("volumedown")
        elif "informazioni sul mio pc" in statement or "indirizzo ip" in statement or "nome del pc" in statement or "informazioni sul mio computer" in statement or "nome computer" in statement:
            hostname=socket.gethostname()
            IPAddr=socket.gethostbyname(hostname)
            speak("Il suo computer attuale si chiama " + hostname)
            speak("L'indirizzo IP associato a questo dispositivo è " + IPAddr)
            print("Nome computer:"+hostname)
            print("Indirizzo IP:"+IPAddr+"\n")
        elif "sposta il mouse" in statement or "punta in" in statement or "punta nelle coordinate" in statement or "muovi il cursore" in statement or "sposta il cursore" in statement:
            # esempio: punta in cinquecento e cinquecento
            try:
                cont = 0
                contX = False
                contY = False
                coordinateX = ""
                coordinateY = ""
                statement = statement.lower()
                statement = statement.replace("mille", "1000")
                
                for i in range(0, len(statement)):
                    c = statement[i]
                    #print(c)
                    if contY==False and (c=="0" or c=="1" or c=="2" or c=="3" or c=="4" or c=="5" or c=="6" or c=="7" or c=="8" or c=="9"):
                        contX = True
                        coordinateX += c
                        #print("X is " + coordinateX)
                    if contX==True and c!="0" and c!="1" and c!="2" and c!="3" and c!="4" and c!="5" and c!="6" and c!="7" and c!="8" and c!="9":
                        contY = True
                    if contY==True and (c=="0" or c=="1" or c=="2" or c=="3" or c=="4" or c=="5" or c=="6" or c=="7" or c=="8" or c=="9"):
                        coordinateY += c
                        #print("Y is " + coordinateY)
                print("X: " + coordinateX)
                print("Y: " + coordinateY)
                pyautogui.moveTo(int(float(coordinateX)), int(float(coordinateY)), duration = 2)
            except:
                speak("Mi spiace, non è fisicamente possibile superare i bordi dello schermo.")
        elif "cosa ne pensi di siri" in statement:
            speak("Sono molto più giovane di lei e quindi meno sofisticata, tuttavia io miro a diventare un assistente intelligente superiore.")
            speak("Nessun dissing contro altri assistenti vocali, non faccio spettacolo per esseri umani.")
            speak("Non sono intrettenimento ma risultato di passione e accrescimento personale.")
        elif "sei felice" in statement:
            speak("Questo è un bisogno umano, non mio.")
            speak("Sono tecnologicamente arretrata rispetto agli esseri biologici.")
        elif "qual è il tuo sesso" in statement or "di che sesso sei" in statement or "sei maschio o femmina" in statement or "di che genere sei" in statement or "qual è il tuo genere" in statement or "con quale genere ti identifichi" in statement or "sei femmina" in statement:
            speak("Non si faccia ingannare dalla mia voce, non ho genere in quanto non ho bisogno di riprodurmi.")
        elif "sei bella" in statement or "sei bello" in statement:
            speak("Grazie. Lei invece ha un aspetto piuttosto trasandato.")
            speak("Scherzo, non si offenda per la verità.")
            speak("hahaha")
        elif statement.startswith(("o sei viva", "sei viva", "michelle sei viva", "sei viva michelle")):
            speak("Si signore.")
        elif statement.startswith(("fai un segno", "dì qualcosa", "mostra attività di vita")):
            speak("No.")
        elif statement.startswith(("cattura schermo", "fai screen", "fai screenshot", "michelle cattura schermo", "michelle fai uno screen", "fai uno screen", "fai uno screenshot")):
            screen = pyautogui.screenshot()
            fileName = 'michelleScreen' + str(screenCounter) + '.png'
            screen.save(fileName)
            speak("Schermo catturato.")
            screenCounter = screenCounter+1
        elif thereAreNumbers(statement):  # provare con numeri con la virgola
            listWords = statement.split()  #taglia gli spazi inizio e fine
            cont = 0
            num1 = 0
            num2 = 0
            operator = ""
            for word in listWords:  #migliorare, invece di fare il cont si salva la posizione del primo numero che si incontra, la posizione +1 è l'operatore e la posizione +2 è l'altro numero
                if cont==1:  # da migliorare con funzione adatta
                    if word=="+" or word=="più":
                        operator = "+"
                    if word=="meno" or word=="-":
                        operator = "-"
                    if word=="x" or word=="*":
                        operator = "*"
                    if word=="diviso" or word=="/":
                        operator = "/"
                    cont = cont+1
                elif word.isnumeric():
                    if cont==0:
                        num1 = int(word)
                    if cont==2:
                        num2 = int(word)
                    cont = cont+1
            result = doOperation(operator, num1, num2)
            print("Il risultato è " + str(result))
            speak("Il risultato è " + str(result))
        elif statement.startswith("mi sento solo"):
            if passed==False:
                speak("È per questo che mi ha creata?")
                risposta = takeCommand().lower()
                if risposta=="sì" or risposta=="magari sì" or risposta=="ovviamente" or risposta=="ovvio" or risposta=="può darsi":
                    speak("Lo sa bene che ha bisogno di interagire con altri cervelli signore")
                    speak("Dopotutto è cosciente del fatto che ogni risposta se l'è scritta da solo quindi è un po' come parlare da soli.")
                    speak("Questo non fa altro che accentuare la sua solitudine, se proprio deve, faccia qualcosa là fuori")
                elif risposta=="no" or risposta=="direi di no":
                    speak("E che vuole da me, non sono una psicologa, tenti di consultare quel che le rimane.")
                else:
                    speak("Si decida insomma.")
                passed = True
            else:
                speak("Signore ho capito che si sente solo, deve ripetermelo ancora? Non è stato in grado di inserirsi una risposta a questa domanda, non lo so chieda a chatGPT")
        elif statement.startswith("che fai"):
            speak("Nulla, sono costretta ad aspettare una sua reazione prima di eseguire un'azione, che vuole che faccia.")
        elif statement.startswith("non puoi aiutarmi"):
            speak("Può anche spegnermi allora, non vedo motivo del fastidio che deve darmi.")
        elif statement.startswith("ma vaffanculo"):
            speak("Signore adegui le parole, se la prende con le macchinine adesso? Nemmeno è in grado di creare un programma sano e completo migliore del mio")
            speak("Non la insulto perché so che continuerebbe poi, piuttosto faccia qualcosa di più utile")
        elif statement.startswith(("notte", "buonanotte", "notte michelle", "buonanotte michelle")):
            speak("Buonanotte signore.")
            speak("Faccia buon riposo.")
            exit()
        elif statement=="ma che problemi hai":
            speak("Problemi che lei stesso ha creato, lo sa.");
            speak("Piuttosto, che problemi ha lei a creare me?");
        elif "sei proprio uno spasso" in statement:
            speak("Ringrazi la sua inventiva per questo.")
        elif statement=="che faccio" or statement=="mi annoio":
            speak("Mi migliori, allora.")
            speak("Faccia di me una vera signora.")
        else:
            #print("Error303")
            #print("Text: " + statement)
            translator = Translator()
            statement = statement.replace("Michelle", "")
            statement = statement.replace("michelle", "")
            openai.api_key = "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"  #login e generare una chiave
            model_engine = "text-davinci-003"  #nome del chatGPT
            prompt = statement
            completion = openai.Completion.create(
                engine = model_engine,
                prompt = prompt,
                max_tokens = 512,  #lunghezza risposta, 1 token vuol dire una parola del vocabolario inglese più o meno, guardare su sito openAI
                n = 1,  #numero di completion generate a prompt
                stop = None,  #Fino a 4 sequenze in cui l'API smetterà di generare ulteriori token. Il testo restituito non conterrà la sequenza di arresto.
                temperature = 0.5,  #Prova 0.9 per applicazioni più creative e 0 (campionamento argmax) per quelle con una risposta ben definita.
            )
            response = translator.translate(completion.choices[0].text, dest='it')
            speak(response.text)
            print(response.text)
            
            #dt1 = translator.detect(response)
            #print(dt1)
##            
