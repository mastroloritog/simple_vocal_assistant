# source code of Samantha, created by @gianzo

from pyttsx3 import init
from speech_recognition import Recognizer, Microphone
from datetime import datetime
import webbrowser
from random import choice

engine = init()
# elsa di default
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[-1].id)
engine.say("Salve, signore, ha appena avviato Samantha.")  #output vocale
engine.runAndWait()  #output vocale
r = Recognizer()

# riconoscimento da microfono
while True:
    with Microphone() as source:
        # testo indica ciò che capisce, risposta ciò che dice

        #while not ValueError or n==0:
        print("Pronta ad ascoltare...")
        audio = r.listen(source)  # limite di ascolto: phrase_time_limit=7
        testo = r.recognize_google(audio, language = 'it-IT')
        
        while UnknownValueError:
            print("Pronta ad ascoltare...")
            audio = r.listen(source, phrase_time_limit=7)
            testo = r.recognize_google(audio, language = 'it-IT')
        
        risposta = "Mi scusi signore, si è verificato un problema con l'ascolto al microfono."   # di default viene messa l'impostazione di non aver compreso il messaggio
        print("Testo: " + testo)

        

        if testo.startswith(("samantha stop", "spegniti samantha", "arresto adesso", "stoppa tutto", "break", "sam stop", "sam spegniti", "spegniti sam", "samantha spegniti")):
            break  # termine ciclo di ascolto
        elif "crea un file di testo" in testo:
            with open("testo.txt", "w") as f:
                f.write("File creato:")
            risposta = "Ecco a lei il file, signore."
        elif any(parola in testo for parola in ["ore", "orario"]):
            now = datetime.now()   # current time
            time = now.strftime('%H:%M')   #hour e minute in stringa
            risposta = "sono le ore " + time
        elif "apri google" in testo:
            webbrowser.open("www.google.com")
            risposta = "Ecco a lei."
        elif testo.startswith(("buongiorno", "buongiornissimo", "bonjour")):
            risposta = choice(["Buongiorno a lei sir, cosa desidera?", "Per fortuna, anche oggi si è alzato sir.", "Vuole del caffé?"])  #random
        elif testo.startswith(("buonasera", "sera")):
            risposta = choice(["Buonasera sir, giornata faticosa?", "Buonasera a lei, signore"])  #random
        elif testo.startswith("sam racconta una barzelletta nera"):
            risposta = choice(["Ad una bambina in Africa le sono arrivate le medicine per l'ebola ma dietro c'è scritto: Da consumare dopo i pasti.",
                               "C'è un bambino cieco. Un giorno i genitori dicono: abbiamo trovato la cura per te, questa sera ti mettiamo questa pomata e domani mattina ci vedrai di nuovo. La mattina dopo il bambino si sveglia ed urla: babbo, mamma, sono sempre cieco! e i genitori rispondono: pesce d'aprile! Pesce d'aprile!",
                               "Una bambina senza braccia dice alla mamma:- mamma, mamma.. posso cambiare vestito di carnevale quest'anno?e la mamma risponde:- perchè, non ti piace più il tuo vestito da ghiacciolo?",
                               "A Lourdes uno seduto in carrozzina si alza in piedi con grande sforzo: Madonna fammi la grazia fammi tornare a casa a piedi...si gira e gli hanno rubato la carrozzina. ",
                               "Papà oggi ho usato per la prima volta la moto. Vuoi sapere com'è andata o preferisci leggerlo domani sul giornale?",
                               "nonna, sento odore di morte.....nonna?....nonna??",
                               "In un lagher c'è un bambino che sta giocando con della polvere per terra, allora un tedesco lo vede e gli chiede: stai cercando qualcuno?",
                               "C'è un ragazzo di colore che cammina tranquillo per il marciapiede con un pappagallo sulla spalla destra. Dopo una decina di minuti passa un bimbo che alla vista dell'animale si ferma e chiede: Bello, che razza è? e il pappagallo: E' un nero",
                               "Un nero entra in un negozio di scarpe e chiede al commesso un paio di mocassini e il commesso dice: li vuole scuri testa di moro? e il nero risponde: no, li voglio bianchi testa di cazzo!",
                               "ci sono tre paracadutisti, uno è tedesco l'altro è francese è l'altro ancora è italiano. il tedesco si butta e dice : viva la germania. si butta il francese e dice : viva la francia. si butta l'italiano , non si  apre il paracadute e dice : viva sta minchia."])
        elif testo.startswith("prova audio"):
            risposta = "L'audio funziona in modo corretto"
        
        engine.say(risposta)   #output vocale
        engine.runAndWait()  #output vocale

risposta = "Spegnimento in corso... alla prossima sir"
engine.say(risposta)   #output vocale
engine.runAndWait()  #output vocale

# print voci disponibili
# voices = engine.getProperty("voices")
# for  voice in voices:
#    print(voice)
