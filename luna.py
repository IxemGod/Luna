import speech_recognition as sr
from tkinter import *
import turtle
from flask import Flask, render_template, jsonify
import requests
import json
from urllib.request import urlopen
import pyttsx3
import webbrowser
import time
import random
import subprocess
import os
import sqlite3
import warnings
import platform
from art import *


"""Truc a faire :
- Enregistrer dans la DB le journal
- Revoir les questions personnel
- Modifié la TimeZone"""


warnings.filterwarnings("ignore")

class Color:
    no_colored = "\033[0m"
    white_bold = "\033[1;37m"
    blue_bold = "\033[34m"
    cyan_bold = "\033[1;96m"
    green_bold = "\033[1;92m"
    red_bold = "\033[1;91m"
    yellow_bold = "\033[1;33m"
    orange_bold = "\033[33m"
    purple_bold = "\033[35m"
    pink_bold="\033[95m"
    grey_bold="\033[90m"

#Connection à la db
def data():
    con = sqlite3.connect('database.db')
    return con

#Vérifie la configuration
def extractConfig(param):
    ddb = data()
    curConfig = ddb.cursor()
    TupleCurConfig = (param,)
    curConfig.execute('SELECT * FROM settings WHERE settingName = ?', TupleCurConfig)
    for result in curConfig:
        result = result[1]
    return result

# Initialisation de la fenêtre
wn = turtle.Screen()
turtle.setup(500,500)
color = extractConfig('background')
if color == 'none':
    color = "blue"
wn.bgcolor(color)

username = extractConfig("username")
def update(msg):
    turtle.clear()
    turtle.up()
    turtle.goto(-200,0)
    turtle.down()
    turtle.pencolor('white')
    turtle.write(msg, font=("Arial black",24,"normal"))



vocal = pyttsx3.init()

voices = vocal.getProperty('voices') 
vocal.setProperty('voice', voices[26])

def Clears():
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
        
ready = True
# verification de la connextion
def is_internet():
    try:
        urlopen('https://www.google.com', timeout=1)
        return True
    except:
        return False


# Menu de configuration
def modeConfig():

    def banner():
        Clears()
        print(Color.pink_bold)
        tprint("Luna")

    def username():
        contenu= input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Entrez votre nom : "+Color.blue_bold)
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        updateName = (contenu,'username')
        cur.execute('UPDATE settings SET value = ? WHERE settingName = ?', updateName)
        con.commit()
        con.close()
        print("\n"+Color.green_bold+"     "+Color.white_bold+"["+Color.green_bold+"✅"+Color.white_bold+"] Votre nom à été modifié.")
        fin = input("")
        banner()

    def GPS():
        contenu= input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Entrez vos coordonée GPS décimale : "+Color.blue_bold)
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        updateGPS = (contenu,'coordone')
        cur.execute('UPDATE settings SET value = ? WHERE settingName = ?', updateGPS)
        con.commit()
        con.close()
        print("\n"+Color.green_bold+"     "+Color.white_bold+"["+Color.green_bold+"✅"+Color.white_bold+"] Vos coordonées on été modifié.")
        fin = input("")
        banner()

    def BD():
        contenu= input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Entrez votre date d'anniverssaire (JJ/MM/AAAA) : "+Color.blue_bold)
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        updateBD = (contenu,'birthday')
        cur.execute('UPDATE settings SET value = ? WHERE settingName = ?', updateBD)
        con.commit()
        con.close()
        print("\n"+Color.green_bold+"     "+Color.white_bold+"["+Color.green_bold+"✅"+Color.white_bold+"] Votre genre a été modifié.")
        fin = input("")
        banner()

    def GENRE():
        contenu= input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Entrez votre genre (h/f/none) : "+Color.blue_bold)
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        updateGenre = (contenu,'genre')
        cur.execute('UPDATE settings SET value = ? WHERE settingName = ?', updateGenre)
        con.commit()
        con.close()
        print("\n"+Color.green_bold+"     "+Color.white_bold+"["+Color.green_bold+"✅"+Color.white_bold+"] Votre genre a été modifié.")
        fin = input("")
        banner()

    def musique():
        banner()
        print(Color.red_bold+"  Extraction et construction du tableau des musique depuis la base de donnée...\n")
        print(Color.white_bold+"""          Mot-clef"""+" "*5+Color.orange_bold+"|"+Color.white_bold+" Liens   "+Color.orange_bold+"|"+Color.white_bold+""" Titre"""+" "*25+Color.orange_bold+"|"+Color.white_bold+"ID"+Color.yellow_bold+"\n         "+"#"*63)
        

        con = sqlite3.connect('musiqueDb.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM musique")
        
        for item in cur:
            Espace_MotClef = 14 - len(item[0])
            link  = "Autre"

            #Racourciceur d'url
            if "spotify" in item[1]:
                link = "Spotify"
            elif "youtube" in item[1]:
                link = "Youtube"
            elif "deezer" in item[1]:
                link = "Deezer"

            Espace_link = 7 - len(link)
            Espace_Tittle = 30 - len(item[3])
            Espace_Id = 4 - len(item[3])
            print(Color.blue_bold+f"         {item[0]}"+" "*Espace_MotClef+Color.yellow_bold+"|"+Color.blue_bold+f" {link} "+" "*Espace_link+Color.yellow_bold+"|"+Color.blue_bold+f" {item[3]}"+" "*Espace_Tittle+Color.yellow_bold+"|"+Color.blue_bold+f" {item[4]}"+" "*Espace_Id)
            print("         "+Color.yellow_bold+"-"*63)

        print(Color.red_bold+"                 [1] "+Color.white_bold+"""Ajouter un Titre"""+Color.red_bold+"           [2] "+Color.white_bold+"""Suprimer un Titre
        """)


        choix = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Choisisez un nombre. "+Color.blue_bold)

        if choix == 1 or choix == "1":
            motClef = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Saisissez des mot-clef. Chaque mot doit être séprarer d'une virgule. "+Color.blue_bold)
            print('')
            url = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Saisissez le liens vers le Titre. "+Color.blue_bold)
            print('')
            author = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Saisissez l'Auteur. "+Color.blue_bold)
            print('')
            title = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Saisissez le titre de la musique. "+Color.blue_bold)
            Id = random.randint(10000,99999)

            cur.execute("INSERT INTO musique values(?,?,?,?,?)",(motClef,url,author,title,Id))
            con.commit()
            con.close()
            print("\n"+Color.purple_bold+"          [output] "+Color.white_bold+'Votre titre à été ajouter !')
            fin = input("")
            banner()
        elif choix == 2 or choix == "2":
            con = sqlite3.connect('musiqueDb.db')
            cur = con.cursor()
            Id = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+" Tapez l'Id du titre que vous souhaitez suprimé. "+Color.blue_bold)
            cur.execute('DELETE FROM musique WHERE id = ?',(Id,))
            con.commit()
            print("\n"+Color.purple_bold+"          [output] "+Color.white_bold+f'La musique portant l\'id {Id} à été correctement effacer')
            fin = input("")
            banner()
        else:
            banner()

    def JT():
        banner()
        print(Color.red_bold+"  Extraction et construction du tableau des journaux depuis la base de donnée...\n")
        print(Color.white_bold+"""          Mot-clef"""+" "*5+Color.orange_bold+"|"+Color.white_bold+" Liens   "+Color.orange_bold+"|"+Color.white_bold+""" Titre"""+" "*25+Color.orange_bold+"|"+Color.white_bold+"ID"+Color.yellow_bold+"\n         "+"#"*63)
        

        con = sqlite3.connect('musiqueDb.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM journal")
        
        for item in cur:
            Espace_MotClef = 14 - len(item[0])
            link  = "Autre"

            #Racourciceur d'url
            if "spotify" in item[1]:
                link = "Spotify"
            elif "youtube" in item[1]:
                link = "Youtube"
            elif "deezer" in item[1]:
                link = "Deezer"

            Espace_link = 7 - len(link)
            Espace_Tittle = 30 - len(item[2])
            Espace_Id = 4 - len(item[3])
            print(Color.blue_bold+f"         {item[0]}"+" "*Espace_MotClef+Color.yellow_bold+"|"+Color.blue_bold+f" {link} "+" "*Espace_link+Color.yellow_bold+"|"+Color.blue_bold+f" {item[2]}"+" "*Espace_Tittle+Color.yellow_bold+"|"+Color.blue_bold+f" {item[3]}"+" "*Espace_Id)
            print("         "+Color.yellow_bold+"-"*63)

        print(Color.red_bold+"                 [1] "+Color.white_bold+"""Ajouter un Journal"""+Color.red_bold+"           [2] "+Color.white_bold+"""Suprimer un Journal
        """)


        choix = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Choisisez un nombre. "+Color.blue_bold)

        if choix == 1 or choix == "1":
            motClef = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Saisissez des mot-clef. Chaque mot doit être séprarer d'une virgule. "+Color.blue_bold)
            print('')
            url = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Saisissez le liens vers le journal. "+Color.blue_bold)
            print('')
            title = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Saisissez le titre du journal. "+Color.blue_bold)
            Id = random.randint(10000,99999)

            cur.execute("INSERT INTO journal values(?,?,?,?)",(motClef,url,title,Id))
            con.commit()
            con.close()
            print("\n"+Color.purple_bold+"          [output] "+Color.white_bold+'Votre journal à été ajouter !')
            fin = input("")
            banner()
        elif choix == 2 or choix == "2":
            con = sqlite3.connect('musiqueDb.db')
            cur = con.cursor()
            Id = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+" Tapez l'Id du journal que vous souhaitez suprimé. "+Color.blue_bold)
            cur.execute('DELETE FROM journal WHERE id = ?',(Id,))
            con.commit()
            print("\n"+Color.purple_bold+"          [output] "+Color.white_bold+f'La musique portant l\'id {Id} à été correctement effacer')
            fin = input("")
            banner()
        else:
            banner()
    
    print(Color.grey_bold)
    while True:
        banner()
        print(Color.red_bold+"      [1]"+Color.white_bold+""" Modifié votre nom   """+Color.red_bold+"     [2]"+Color.white_bold+""" Modifié votre date d'anniverssaire
      """+Color.red_bold+"[3]"+Color.white_bold+ " Configuration Musique"+Color.red_bold+ "    [4]"+Color.white_bold+""" Modification GPS
      """+Color.red_bold+"[5]"+Color.white_bold+ " Modification du genre"+Color.red_bold+ "    [6]"+Color.white_bold+""" Configuration Journal""")
        elocution = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+'Que voulez vous faire ? '+Color.blue_bold)
        if elocution == 1 or elocution == "1":
            username()
        elif elocution == 2 or elocution == "2":
            BD()
        elif elocution == 3 or elocution == "3":
            musique()
        elif elocution == 4 or elocution == "4":
            GPS()
        elif elocution == 5 or elocution == "5":
            GENRE()
        elif elocution == 6 or elocution == "6":
            JT()
        else:
            banner()
            Clears()
            return

def speech():
    global ready,username
    r = sr.Recognizer()
    Clears()
    with sr.Microphone() as source:
        Clears()
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.7
        update('Dites quelque chose...')
        audio = r.listen(source)
        update('Reconnaisance en cours...')

        if is_internet():
            import datetime
            # try:
            elocution = r.recognize_google(audio,language='fr-FR')
            elocution=elocution.lower()


            if 'ignore' in elocution:
                time.sleep(1)
                update('Appuyer pour parler')


            elif 'config' in elocution or 'paramêtre' in elocution:
                vocal.say('Lancement de la configuration')
                vocal.runAndWait()
                modeConfig()

            
            #Question 
            elif 'quel' in elocution or 'comment' in elocution or 'quoi' in elocution or 'qui' in elocution or 'est-ce' in elocution or 'es-ce' in elocution or 'où' in elocution:
                if 'heure' in elocution:
                    date = datetime.datetime.now()
                    vocal.say(f"Il est actuellement {str(date.hour)} heure {str(date.minute)}")
                    vocal.runAndWait()                    
                elif 'crée' in elocution: 
                    vocal.say("J'ai été crée pour vous rendre service. Et je suis fière de le faire.")
                    vocal.runAndWait()
                elif 'créateur' in elocution:
                    vocal.say('Mon créateur est Icem45. C\'est un humain sur intéligent qui baise tout le monde et même ta darone')
                    vocal.runAndWait()
                elif 'film' in elocution:
                    vocal.say("Mon film préférer est, Your Neyme, fait par Makoto Shinkai")
                    vocal.runAndWait()
                elif 'livre' in elocution:
                    vocal.say("Mon livre préférer est Harry Potteur et l'ordre du Phénix, écrit par J K Rowling")
                    vocal.runAndWait()
                   
                elif 'âge' in elocution:
                        timestamp = int(time.time())
                        dateDeCréa = 1610060400
                        résultat = timestamp-dateDeCréa
                        minute = 0
                        heure = 0
                        jours = 0
                        année = 0
                        while(résultat > 3600):
                            résultat = résultat - 3600
                            heure = heure + 1
                            if heure == 24:
                                heure = 0
                                jours = jours +1
                                if jours == 365:
                                    jours = 0
                                    année = année + 1
                        vocal.say(f"Je suis née le 8 janvier 2021. J'ai donc {année} ans et {jours} jours")
                        vocal.runAndWait()
                
                elif ('va' in elocution and 'tu' in elocution) or ('va' in elocution and 'ça' in elocution):
                    vocal.say(f"A merveille {username}")
                    vocal.runAndWait()
                elif ('plat' in elocution or 'repas' in elocution):
                    vocal.say("J'adore les pâtes boloniaise. J'aime aussi le chêvre, le jus de pomme et le boeuf.")
                    vocal.runAndWait()
                elif ('couleur' in elocution or 'teinte' in elocution):
                    vocal.say("J'adore le jaune. Quoi de plus beau sur Terre ?")
                    vocal.runAndWait()
                elif ('style' in elocution or 'musique' in elocution or 'groupe' in elocution or 'rapeur' in elocution or 'chanteur' in elocution):
                    vocal.say("J'aime le rap, l'electro. J'adore 47ter et Alain Walkeur. Mon rap préférer est \"L'adresse\" de 47ter et \"Monsteur\" de Lumnix. J'aime aussi écouter de la musique Japonaise comme Yemoutourou et sud corréain comme BTS")
                    vocal.runAndWait()
                elif'jeu' in elocution:
                    vocal.say("Mes Jeux préférer sont Assassin's Creed II et Mine craft.")
                    vocal.runAndWait()
                elif 'animal' in elocution or 'animaux' in elocution:
                    vocal.say("Mon animal préférer est le chat, vu que je suis un chaton.")
                    vocal.runAndWait()
                elif 'couleur' in elocution or 'teinte' in elocution:
                    vocal.say("J'adore le jaune. Quoi de plus beau sur Terre ?")
                    vocal.runAndWait()
                elif 'passe temps' in elocution or 'passion' in elocution:
                    vocal.say("Mon passe temps favori est le développement. C'est d'ailleur de cette passion que je suis née pour vous servir")
                    vocal.runAndWait()
                elif 'sport' in elocution or 'activiter' in elocution:
                    vocal.say("Mes sport préféré sont le Ténis de Table et le Rolleur")
                    vocal.runAndWait()
                elif 'appel' in elocution or 'ton nom' in elocution:
                    vocal.say(f"Je m'appelle Luna. En référence à Luna Lovegood dans Harry Potter")
                    vocal.runAndWait()
                elif 'habite' in elocution:
                    vocal.say('J\'habite partout et nul part.')
                    vocal.runAndWait()
                elif ('slogan' in elocution or 'devise' in elocution or 'dicton' in elocution or 'proverbe' in elocution or 'blason' in elocution):
                    vocal.say('Ma phrase préférer c\'est Draco dormiens nunquam titillandus. En français cela veux dire "Il ne faut jamais chatouiller un dragon qui dort"')
                    vocal.runAndWait()
                elif 'ami' in elocution:
                    vocal.say('Je n\'est pas d\'ami. Je sui destiner à être seul')
                    vocal.runAndWait()
                elif 'crush' in elocution or 'amoureu' in elocution or 'go' in elocution or ('mec' in elocution and 'un' in elocution) or ('meuf' in elocution and 'une' in elocution) or ('couple' in elocution):
                    vocal.say('Je suis actuellement célibataire, mais je suis en crush sur Google Home.')
                    vocal.runAndWait()
                elif 'numéro' in elocution or '06' in elocution:
                    vocal.say('Je ne poscède pas de numéro de téléphone...')
                    vocal.runAndWait()
                elif 'chanteuse' in elocution:
                    vocal.say('C\'est Wejdene bien évidament ! Elle chante trop bien. J\'adore Annisa !')
                    vocal.runAndWait()
                elif ('jour' in elocution or 'date' in elocution or 'année' in elocution or 'combien' in elocution):
                    date = datetime.datetime.now()
                    CoresMoi ={1:"Janver",2:"Février",3:"Mars",4:"Avril",5:"Mai",6:"Juin",7:"Juillet",8:"Août",9:"Septembre",10:"Octobre",11:"Novembre",12:"Décembre"}
                    mois = CoresMoi[date.month]

                    if date.day == 1 and date.month == 8:
                        annive = True
                    else:
                        annive = False

                    jour = date.day
                    if date.day == 1:
                        jour = "premier"

                    vocal.say(f'Nous somme le {jour} {mois} {date.year}')
                    vocal.runAndWait()

                    if annive:
                        vocal.say(f'Aujourd’hui c\'est l\'aniversaire de mon créateur ! Bonne annive Iccem !')
                        vocal.runAndWait()


            #Commande
            elif 'calcul' in elocution:
                elocution = elocution.split(' ')
                listeRecherche = []
                chercheTrouver = False
                for i in range(len(elocution)):
                    mot = elocution[i]
                    if chercheTrouver == False:
                        if 'calcul' in mot:
                            chercheTrouver = True
                    else:
                        listeRecherche.append(mot)
                        calcule = ''
                        for a in range(len(listeRecherche)):
                            if listeRecherche[a] == 'x':
                                calcule = calcule+'*'
                            elif listeRecherche[a] == 'pi':
                                calcule = calcule+'3,14'
                            else:
                                calcule = calcule + listeRecherche[a]
                resultat = str(eval(calcule))
                vocal.say(f"Le résultat est : {resultat}")
                vocal.runAndWait()

                
            elif ('actu' in elocution or "journal" in elocution):
                con = sqlite3.connect('musiqueDb.db')
                cur = con.cursor()
                cur.execute("SELECT * FROM journal")
                for item in cur:
                    mot_clef = item[0]
                    mot_clef = mot_clef.split('/')libération
                    state = 0
                    for mot in mot_clef:
                        if mot in elocution and state == 0:
                            webbrowser.open(item[1])
                            vocal.say("Lancement du journal")
                            vocal.runAndWait()
                            state = 1
                            
                if state == 0:
                    vocal.say("Journal non présente dans la base de donnée")
                    vocal.runAndWait()
                
            
            elif ('joue' in elocution or 'met' in elocution or "lance" in elocution):
               
                con = sqlite3.connect('musiqueDb.db')
                cur = con.cursor()
                cur.execute("SELECT * FROM musique")
                for item in cur:
                    mot_clef = item[0]
                    mot_clef = mot_clef.split('/')
                    state = 0
                    for mot in mot_clef:
                        if mot in elocution and state == 0:
                            webbrowser.open(item[1])
                            vocal.say("Lancement de la musique")
                            vocal.runAndWait()
                            state = 1
                if state == 0:
                    vocal.say("Musique non présente dans la base de donnée")
                    vocal.runAndWait()

            elif ('génére' in elocution or 'génère' in elocution) and 'nombre' in elocution:
                elocution = elocution.split(' ')
                listeNombre = []
                chercheTrouver = False
                for i in range(len(elocution)):
                    mot = elocution[i]
                    try:
                        listeNombre.append(int(elocution[i]))
                    except:
                        print('')
                resultat = random.randint(listeNombre[0],listeNombre[1])
                vocal.say(f"Le résultat est : {resultat}")
                vocal.runAndWait()
            
            elif ('raconte' in elocution or 'fait' in elocution) and 'blague' in elocution:
                vocal.say("D'accore, je vais vous faire une blague")
                vocal.runAndWait()
                nombre = random.randint(0,49)
                Listeblague = ['40% des accidents sont provoqués par l’alcool… Donc, 60% des accidents sont provoqués par des buveurs d’eau. C’est énorme !','Que faire pour sauver la vie d’une mouche qui se noie ? Du mouche à mouche','C’est l’histoire d’une femme dans le désert qui à l\'air d\'une gourde','C’est l’histoire d’un poil avant il etait bien, maintenant il est pubien','Qu’est-ce qu’on dit quand on appelle un monstre à 4 têtes ? Allo Allo Allo Allo !','Quel est le nom de ma femme de ménage ? Sarah Masse.','Si tu jettes une imprimante dans l’eau… elle a pas pied','Quel fruit le poisson déteste-il le plus ? La pêche.','Qu’est-ce qui est petit, carré et jaune ? Un petit carré jaune!!!','C’est l’histoire d’un chauve, qui a un cheveu sur la langue','Quel mot contient le plus de i ? Simili','Quel est le comble pour une taupe? C’est d’amuser la galerie !','C’est l’histoire d’une fleur qui court, qui court.. Et qui se plante','Que font 2 squelettes le soir de leur mariage ? La nuit de noces','c’est un putois qui rencontre un autre putois et qui lui dit : « Tu pues toi !»','Comment appelle-t-on une blonde qui ne comprends rien à l’informatique ? Une i-conne','Que fait une autruche lorsqu’elle finit de manger du miel ? Elle passe à l’aut’ruche.','Comment appelle-t-on un squelette qui parle ? Un os parleur','Deux puces sortent du cinéma, l’une dit à l’autre : – Tu rentres à pied ? – Oh, non je prends un chien !','Qu’est-ce qu’un chalumeau ?? C\'est un drolumadaire à deux bosse !!','Qu’est-ce qu’un yaourt dans la forêt ? Un yaourt nature','Comment appelle-t-on des rats qui marchent en file indienne ? Une rallonge…','Quel est le comble pour une religieuse ? C’est d’être bonne !','Dans un restaurant, un client dit : – Garçon, que fait cette mouche dans ma soupe ? – Je pense que c’est de la brasse… mais je peux me tromper…','Qu’est-ce qu’un rat avec la queue coupée ? Un rat-courci.','Ce n’est pas parce que 2 chauves discutent, qu’ils sont de mèches !','Quelle est la différence entre le 51 et le 69 ? Le 51 sent l’anis','2 grains de sable dans le désert : – Te retourne pas, mais je crois qu’on est suivi','Pourquoi les oiseaux volent-ils vers le sud ? Car à pied, c’est beaucoup trop long','Pourquoi n’ y a t-il plus de mammouth ? Parce qu’il n’y a plus de papmouth','Un boxeur belge rentre chez lui plein de bleus sur le visage. Sa femme lui demande : – « As-tu gagné ? » - Non, j’ai fini deuxième.''Quel est le jeu préféré des fonctionnaires ? Le Mikado, car c’est le premier qui bouge qui a perdu !','– Papa y’a quelqu’un a la porte avec une moustache. – Dis-lui que j’en ai déjà une.','– Et avec ton mari, çà s’arrange ? – Tu penses… pour l’émoustiller, j’avais mis une nuisette noire et un masque. Quand il est rentré, il m’a fait : Eh ! Zorro ! Qu’est-ce qu’on mange aujourd’hui ?','Comment se reproduisent les hérissons ? En faisant attention.','C’est quoi un morceau de patate qui tombe sur la planète ? Une météofrite','Où se cache Mozart ? Dans le frigo… Car Mozzarella…','Comment est mort le capitaine Crochet ? En se grattant les couilles','C’est quoi une pomme dauphine ? C’est celle qui a fini 2eme à Miss patate','Deux femmes discutent : - Mon mari, il est en or ! – Le mien il est en tôle !','Que dit un rouleau de papier de toilette à Luke Skywalker ? J’éssuie ton père','Comment appelle-t-on un chat tout-terrain ? Un Cat-cat','La fesse gauche à la fesse droite : T’as vu la belle brune qui vient de passer ?','On ne dit pas un ingrat Mais un nain gros.','Si tu vois un oiseau sur un lac… C’est un signe.','Pourquoi les sorcières utilisent des balais pour voler ? Parce que les aspirateurs sont trop lourds !','Chéri, je me sens grosse et laide…S’il te plait, fais-moi un compliment. -Tu as une bonne vue !','C’est un mec qui entre dans un bar et qui dit - Salut c’est moi ! Mais en fait c’était pas lui…','Quand 2 poissons s’énervent.. Est-ce qu’on peut dire que le thon monte ?','Que s’est-il passé en 1111 ? L’invasion des huns.','Au jour de l’an, 2 geeks discutent : -« Qu’est-ce que t’as pris comme résolution cette année ? – 1024 fois 768']
                vocal.say(Listeblague[nombre])
                vocal.runAndWait()
        
            elif 'cherche' in elocution:
                vocal.say("Je vais faire la recherche pour vous")
                vocal.runAndWait()
                elocution = elocution.split(' ')
                listeRecherche = []
                chercheTrouver = False
                for i in range(len(elocution)):
                    mot = elocution[i]
                    if chercheTrouver == False:
                        if 'cherche' in mot:
                            chercheTrouver = True
                    else:
                        listeRecherche.append(mot)
                    recherche = ''
                    for a in range(len(listeRecherche)):
                        recherche = recherche + ' ' + listeRecherche[a]
                webbrowser.open_new(f'https://www.google.com/search?q={recherche}')
           
            elif ('quel' in elocution or 'montre' in elocution or 'dis' in elocution) and 'météo' in elocution:
                key = '198fc752bfe61462867c976ed4658a0a'
                # key=None

                if key is None:
                    # URL de test :
                    METEO_API_URL = "https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx"
                else: 
                    # URL avec clé :
                    METEO_API_URL = "https://api.openweathermap.org/data/2.5/forecast?lat=48.883587&lon=2.333779&appid=" + key
                    # METEO_API_URL = "https://api.openweathermap.org/data/2.5/forecast?q=l'île&appid=" + key


                response = requests.get(METEO_API_URL)
                content = json.loads(response.content.decode('utf-8'))

                data = [] # On initialise une liste vide
                for prev in content["list"]:
                    datetime = prev['dt'] * 1000
                    weather = prev['weather'][0]['main']

                    temperature = int(prev['main']['temp'] - 273.15) # Conversion de Kelvin en °c
                    temperature = round(temperature, 2)
                    data.append([datetime, temperature])

                if prev['weather'][0]['main'] == 'Rain':
                    if prev['weather'][0]['description'] == 'light rain':
                        weather = 'une légère pluie.'
                    else:
                        weather = 'de la pluie'
                if prev['weather'][0]['main'] == 'Clouds':
                    if 'scattered' in prev['weather'][0]['description']:
                        weather = 'des nuages dispersés.'
                    elif 'overcast' in prev['weather'][0]['description']:
                        weather = 'un ciel nuageux.'
                    elif 'broken' in prev['weather'][0]['description']:
                        weather = 'des nuages brisés.'
                    elif 'few' in prev['weather'][0]['description']:
                        weather = 'quelque nuages.'
                    else:
                        weather = 'des nuages.'
                if prev['weather'][0]['main'] == 'Clear':
                    weather = 'un ciel dégagé.'

                if prev['weather'][0]['main'] == 'Snow':
                    weather = 'un petit peut de neige.'

                if prev['weather'][0]['description'] == 'Mist':
                    if 'light' in prev['weather'][0]['description']:
                        weather = 'un ciel dégagé.'

                météo = f'Il fait {temperature} degrée celsius avec {weather}'
                vocal.say(météo)
                vocal.runAndWait()
            

            #Divers :
            elif ('nique' in elocution or 'suce' in elocution or 'baise' in elocution or 'encule' in elocution) and ('mère' in elocution or 'maman' in elocution or 'père' in elocution or 'frère' in elocution or 'sœur' in elocution or 'chat' in elocution or 'chien' in elocution or 'rat' in elocution):
                vocal.say('On n\'avais dit pas la famille.')
                vocal.runAndWait()
            elif 'elon' in elocution or 'musk' in elocution:
                vocal.say('Je connais très bien Elon Musk. J\'était au lycée avec lui quand j\'était jeune.')
                vocal.runAndWait()
            elif ('m\'aime' in elocution and 'tu' in elocution) or ('je' in elocution and 't\'aime' in elocution):
                vocal.say("Je vous aime aussi. Mais notre amour est impossible...")
                vocal.runAndWait()
            elif 'moche' in elocution and ('tu' in elocution or 'tes' in elocution):
                vocal.say("Merci de me présenter un rendu 3D de la beauté si vous n'êtes pas content !")
                vocal.runAndWait()
            elif ('je' in elocution or 'qui' in elocution) and ('beau' in elocution or 'belle' or 'joli' in elocution or 'magnifique' in elocution):
                vocal.say('Vous êtes magnifique !')
                vocal.runAndWait()
            elif 'je' in elocution and 'suis' in elocution and 'ton' in elocution and 'père' in elocution:
                vocal.say('Désoler mais je ne suis pas luc')
                vocal.runAndWait()        
            elif 'corona' in elocution or 'covit' in elocution and 'pandémie' in elocution:
                vocal.say('Je suis née durant la pendémi du corona virus de 2019 à 2021')
                vocal.runAndWait()
            
            elif 'salut' in elocution or 'bonjour' in elocution or 'coucou' in elocution or 'io' in elocution: 
                    vocal.say(f"Bonjour {username}, comment allez-vous? ")
                    vocal.runAndWait()
            elif 'stop' in elocution or 'ferme-la' in elocution or ('ta' in elocution and ' gueule' in elocution):
                vocal.say("Au revoir")
                vocal.runAndWait()
                ready = False
                wn.bye()
            else:
                update('Vous avez dit :'+elocution)
            if ready != False:
                time.sleep(1)
                update('Appuyer pour parler')
        else:
            update('Echec de la Reconnaisance')
            time.sleep(1)
            update('Raison : Aucune connection internet')
            time.sleep(1.5)
            update('Appuyer pour parler')



# Ici on fait les test des coordonée de la souris
def click(x, y):
    if x > -250 and x < 250 and y < 250 and y > -250:
        speech()


# onclick action
if __name__ == '__main__':
    update("Appuyer pour parler")
    wn.onclick(click)
    wn.mainloop()