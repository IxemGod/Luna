import speech_recognition as sr
from urllib.request import urlopen
import pyttsx3
import datetime
import webbrowser
import turtle
import time
import random


# Initialisation de la fenêtre
wn = turtle.Screen()
turtle.setup(500,500)
turtle.speed(20)
wn.bgcolor("blue")

def update(msg):
    turtle.clear()
    turtle.up()
    turtle.goto(-200,0)
    turtle.down()
    turtle.pencolor('white')
    turtle.write(msg, font=("Arial black",24,"normal"))


nom = "chaton"


vocal = pyttsx3.init()
api_adresse = ("api.openweathermap.org/data/2.5/weather?appid=198fc752bfe61462867c976ed4658a0a&q=Mumbai")
#json_data = requests.get(api_adresse).json()
#print(json_data)


#python C:/Users/Ixem4/PycharmProjects/main/venv/IA.py

ready = True
# verification de la connextion
def is_internet():
    try:
        urlopen('https://www.google.com', timeout=1)
        return True
    except:
        return False
    return True

def speech():
    global ready
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.7
        update('Dites quelque chose...')
        audio = r.listen(source)
        update('Reconnaisance en cours...')

        if is_internet():
            try:
                elocution = r.recognize_google(audio,language='fr-FR')
                elocution=elocution.lower()
                print(elocution)

                #Les information sur la personaliter du bot
                if 'salut' in elocution:
                    vocal.say("Bonjour Iccem, comment allez-vous? ")
                    vocal.runAndWait()
                elif 'qui' in elocution and 'créateur' in elocution:
                    vocal.say("Mon créateur est Iccem45")
                    vocal.runAndWait()
                elif 'quel' in elocution and 'film' in elocution:
                    vocal.say("Mon film préférer est, Your Neyme, fait par Makoto Shinkai")
                    vocal.runAndWait()
                elif 'quel' in elocution and 'livre' in elocution:
                    vocal.say("Mon livre préférer est Harry Potteur et l'ordre du Phénix, écrit par J K Rowling")
                    vocal.runAndWait()
                elif 'quel' in elocution and 'âge' in elocution:
                    vocal.say("Je suis née le 8 janvier 2021")
                    vocal.runAndWait()

                    timestamp = int(time.time())
                    dateDeCréa = 1610060400
                    print(timestamp)
                    résultat = timestamp-dateDeCréa
                    #résultat = résultat*(-1)
                    print(résultat)
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
                    vocal.say(f"J'ai donc {année} ans, et {jours} jours")
                    vocal.runAndWait()
                    print(f'J\'ai {année} ans et {jours} jours')
                elif ('comment' in elocution and 'va' in elocution and 'tu' in elocution) or ('va' in elocution and 'ça' in elocution and nom in elocution):
                    vocal.say("A merveille Iccem")
                    vocal.runAndWait()
                elif 'qui' in elocution and 'patron' in elocution and 'est' in elocution:
                    vocal.say("C'est vous évidement !")
                    vocal.runAndWait()
                elif 'tu' in elocution and 'es' in elocution and ('ia' in elocution or 'intelligence' in elocution):
                    vocal.say("Je suis plutôt un programme qui répond à vos question qui sont déjà écrite dans moi.")
                    vocal.runAndWait()
                elif (('quel' in elocution or 'quoi' in elocution) and 'est' in elocution or 'elle' in elocution) and ('plat' in elocution or 'repas' in elocution):
                    vocal.say("J'adore les pâtes boloniaise. J'aime aussi le chêvre, le jus de pomme et le boeuf.")
                    vocal.runAndWait()
                elif (('quel' in elocution or 'quoi' in elocution) and 'est' in elocution or 'elle' in elocution) and ('couleur' in elocution or 'teinte' in elocution):
                    vocal.say("J'adore le jaune. Quoi de plus beau sur Terre ?")
                    vocal.runAndWait()
                elif (('quel' in elocution or 'quoi' in elocution) and 'est' in elocution or 'elle' in elocution) and ('style' in elocution or 'musique' in elocution or 'groupe' in elocution or 'rapeur' in elocution or 'chanteur' in elocution):
                    vocal.say("J'aime le rap, l'electro. J'adore 47ter et Alain Walkeur. Mon rap préférer est \"L'adresse\" de 47ter et \"Monsteur\" de Lumnix. J'aime aussi écouter de la musique Japonaise comme Yemoutourou et sud corréain comme BTS")
                    vocal.runAndWait()
                elif (('quel' in elocution or 'quoi' in elocution) and 'est' in elocution or 'elle' in elocution) and ('jeu' in elocution):
                    vocal.say("Mes Jeux préférer sont Assassin's Creed II et Mine craft.")
                    vocal.runAndWait()
                elif (('quel' in elocution or 'quoi' in elocution) and 'est' in elocution or 'elle' in elocution) and ('animal' in elocution or 'animaux' in elocution):
                    vocal.say("Mon animal préférer est le chat, vu que je suis un chaton.")
                    vocal.runAndWait()
                elif (('quel' in elocution or 'quoi' in elocution) and 'est' in elocution or 'elle' in elocution) and ('couleur' in elocution or 'teinte' in elocution):
                    vocal.say("J'adore le jaune. Quoi de plus beau sur Terre ?")
                    vocal.runAndWait()
                elif (('quel' in elocution or 'quoi' in elocution) and 'est' in elocution or 'elle' in elocution) and ('passe temps' in elocution or 'passion' in elocution):
                    vocal.say("Mon passe temps favori est le développement. C'est d'ailleur de cette passion que je suis née pour vous servir")
                    vocal.runAndWait()
                elif (('quel' in elocution or 'quoi' in elocution) and 'est' in elocution or 'elle' in elocution) and ('sport' in elocution or 'activiter' in elocution):
                    vocal.say("Mes sport préféré sont le Ténis de Table et le Rolleur")
                    vocal.runAndWait()
                elif ('comment' in elocution and 'tu' in elocution and 'appelle' in elocution) or ('quel' in elocution and 'est' in elocution and 'ton nom' in elocution):
                    vocal.say(f"Je m'appelle {nom}")
                    vocal.runAndWait()


                #Commande
                elif 'calcul' in elocution:
                    elocution = elocution.split(' ')
                    print(elocution)
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
                    print(calcule)
                    resultat = str(eval(calcule))
                    vocal.say(f"Le résultat est : {resultat}")
                    vocal.runAndWait()
                elif ('actu' in elocution):
                    vocal.say("Qu'elle press voulez vous lire ?")
                    vocal.runAndWait()
                    update("Dites quelque chose...")
                    print("....")
                    audio = r.listen(source)
                    update("Reconnaisance en cours...")
                    elocution = r.recognize_google(audio,language='fr-FR')
                    elocution=elocution.lower()
                    print(elocution)
                    if 'ouest'in elocution and 'france' in elocution:
                        vocal.say('Je lance le Ouest France sur internet')
                        vocal.runAndWait()
                        webbrowser.open_new('https://www.ouest-france.fr')
                    elif 'parisien'in elocution:
                        vocal.say('Je lance le Parisien sur internet')
                        vocal.runAndWait()
                        webbrowser.open_new('https://www.leparisien.fr')
                    elif 'monde'in elocution:
                        vocal.say('Je lance le monde sur internet')
                        vocal.runAndWait()
                        webbrowser.open_new('https://www.lemonde.fr')
                    elif 'figaro'in elocution:
                        vocal.say('Je lance le figaro sur internet')
                        vocal.runAndWait()
                        webbrowser.open_new('https://www.lefigaro.fr')
                    elif 'gorafi'in elocution:
                        vocal.say('Je lance le gorafi sur internet')
                        vocal.runAndWait()
                        webbrowser.open_new('http://www.legorafi.fr')
                    elif 'liberation'in elocution:
                        vocal.say('Je lance liberation sur internet')
                        vocal.runAndWait()
                        webbrowser.open_new('https://www.liberation.fr')
                    elif 'mediapart'in elocution:
                        vocal.say('Je lance médiapart sur internet')
                        vocal.runAndWait()
                        webbrowser.open_new('https://www.mediapart.fr')
                    elif 'point'in elocution:
                        vocal.say('Je lance le point sur internet')
                        vocal.runAndWait()
                        webbrowser.open_new('https://www.lepoint.fr')
                    elif 'obs'in elocution:
                        vocal.say('Je lance l\'OBS sur internet')
                        vocal.runAndWait()
                        webbrowser.open_new('https://www.nouvelobs.com')
                    elif 'france 24'in elocution:
                        vocal.say('Je lance france24 sur internet')
                        vocal.runAndWait()
                        webbrowser.open_new('https://www.france24.com/fr/france/')
                    elif 'opignon'in elocution:
                        vocal.say('Je lance l\'opignon sur internet')
                        vocal.runAndWait()
                        webbrowser.open_new('https://www.lopinion.fr')
                    elif 'echo'in elocution:
                        vocal.say('Je lance les échos sur internet')
                        vocal.runAndWait()
                        webbrowser.open_new('https://www.lesechos.fr')
                    elif 'croix'in elocution:
                        vocal.say('Je lance la croix sur internet')
                        vocal.runAndWait()
                        webbrowser.open_new('https://www.la-croix.com')
                    elif 'humanité'in elocution:
                        vocal.say('Je lance l\'humanité sur internet')
                        vocal.runAndWait()
                        webbrowser.open_new('https://www.humanite.fr')
                    elif 'équipe'in elocution:
                        vocal.say('Je lance l\'humanité sur internet')
                        vocal.runAndWait()
                        webbrowser.open_new('https://www.lequipe.fr')
                elif 'quel' in elocution and 'heure' in elocution:
                    date = datetime.datetime.now()
                    vocal.say(f"Il est actuellement {date.hour} heure {date.minute}")
                    vocal.runAndWait()
                elif ('est' in elocution or'quel' in elocution) and ('jour' in elocution or 'date' in elocution or 'année' in elocution or 'combien' in elocution):
                    date = datetime.datetime.now()
                    annive = False
                    if date.month == 1:
                        mois = 'Janvier'
                    if date.month == 2:
                        mois = 'Février'
                    if date.month == 3:
                        mois = 'Mars'

                    if date.month == 4:
                        mois = 'Avril'

                    if date.month == 5:
                        mois = 'Mai'

                    if date.month == 6:
                        mois = 'Juin'

                    if date.month == 7:
                        mois = 'Juillet'

                    if date.month == 8:
                        mois = 'Août'

                    if date.day == 1:
                        annive = True

                    if date.month == 9:
                        mois = 'Septembre'

                    if date.month == 10:
                        mois = 'Octobre'

                    if date.month == 11:
                        mois = 'Novembre'

                    if date.month == 12:
                        mois = 'Décembre'

                    jour = date.day
                    if date.day == 1:
                        jour = premier

                    vocal.say(f'Nous somme le {jour} {mois} {date.year}')
                    vocal.runAndWait()

                    if annive == True:
                        vocal.say('Bonne anniversaire Iccem ! Profitez de cette journer incroyable')
                        vocal.runAndWait()
                    #Demandement elle va
                elif 'comment' in elocution and 'va' in elocution and 'tu' in elocution:
                    date = datetime.datetime.now()
                    vocal.say("Je suis de la même hummeur que vous")
                    vocal.runAndWait()
                elif ('joue' in elocution or 'met' in elocution) and 'musique' in elocution:


                    vocal.say("D'accore, Qu'elle musique voulez vous que je lance ?")
                    vocal.runAndWait()
                    print("....")
                    update("Dites quelque chose...")
                    audio = r.listen(source)
                    update("Reconnaisance en cours...")
                    elocution = r.recognize_google(audio,language='fr-FR')
                    elocution=elocution.lower()
                    print(elocution)
                    if 'coco' in elocution or 'coucou' in elocution:
                        vocal.say("Je lance Coco de Wejdene sur Spotify")
                        vocal.runAndWait()
                        webbrowser.open_new('https://open.spotify.com/track/593oNiMJ6d9PQkaOLOvIDo')
                    elif 'côte' in elocution or 'ouest' in elocution:
                        vocal.say("Je lance Côte Ouest sur Spotify")
                        vocal.runAndWait()
                        webbrowser.open_new('https://open.spotify.com/track/4ZuuPLV4qYiznagLAFPHcW')
                    elif 'alors alors' in elocution:
                        vocal.say("Je lance Alors Alors de Bigflo et Oli sur Spotify")
                        vocal.runAndWait()
                        webbrowser.open_new('https://open.spotify.com/track/1TAtVjJ9Fx5RLHQv4hmpOR')
                    elif 'your name' in elocution or 'youre name' in elocution:
                        vocal.say("Je lance Yumetourou de Your Name sur Spotify")
                        vocal.runAndWait()
                        webbrowser.open_new('https://open.spotify.com/track/2XDLLEFWTuCRBZy21fRpcm')
                    elif 'docteur' in elocution:
                        vocal.say("Je lance Docteur de La voix sur Spotify")
                        vocal.runAndWait()
                        webbrowser.open_new('https://open.spotify.com/track/6D17z4WZA8HfFsDNmdRAIN')
                    elif 'dans ma tête' in elocution or "tête" in elocution:
                        vocal.say("Je lance Dans ma tête de La voix sur Spotify")
                        vocal.runAndWait()
                        webbrowser.open_new('https://open.spotify.com/track/6Dl8WpvxTQ0agzfPyq3Kcz')
                    elif 'homme' in elocution:
                        vocal.say("Je lance On de BTS sur Spotify")
                        vocal.runAndWait()
                        webbrowser.open_new('https://open.spotify.com/track/1iCJrfkx5U4DtmkazBSYVG')
                    elif 'dynamite' in elocution:
                        vocal.say("Je lance dinamyte de BTS sur Spotify")
                        vocal.runAndWait()
                        webbrowser.open_new('https://open.spotify.com/track/0t1kP63rueHleOhQkYSXFY')
                    elif 'blue' in elocution:
                        vocal.say("Je lance Blue de Eiffel 65 sur Spotify")
                        vocal.runAndWait()
                        webbrowser.open_new('https://open.spotify.com/track/2yAVzRiEQooPEJ9SYx11L3')
                    elif 'mood' in elocution:
                        vocal.say("Je lance Mood de 24kGoldn et Iann dior sur Spotify")
                        vocal.runAndWait()
                        webbrowser.open_new('https://open.spotify.com/track/3tjFYV6RSFtuktYl3ZtYcq')
                    elif 'adresse' in elocution:
                        vocal.say("Je lance L'adresse de 47ter sur Spotify")
                        vocal.runAndWait()
                        webbrowser.open_new('https://open.spotify.com/track/2imn6s1bQUKShiC7Ab2Lp5?si=QTEHmI9sQsi4UTbyjRW5Qw')
                    elif 'tourner' in elocution and 'tête' in elocution:
                        vocal.say("Je lance Tourner la tête de Hornet la Frappe sur Spotify")
                        vocal.runAndWait()
                        webbrowser.open_new('https://open.spotify.com/track/1NfhS4IBo7m6npwPNMkZbJ?si=6HnOcdOYSvm2q-T90iq9nA')
                    elif 'monster' in elocution:
                        vocal.say("Je lance Monster de Lumix sur Spotify")
                        vocal.runAndWait()
                        webbrowser.open_new('https://open.spotify.com/track/0YU17F0BlVXvmx5ytsR43w?si=OU4ivqtCTq-pWnynMr7Kmg')
                    elif 'monster' in elocution:
                        vocal.say("Je lance Monster de Lumix sur Spotify")
                        vocal.runAndWait()
                        webbrowser.open_new('https://open.spotify.com/track/0YU17F0BlVXvmx5ytsR43w?si=OU4ivqtCTq-pWnynMr7Kmg')
                #blague
                elif ('raconte' in elocution or 'fait' in elocution) and 'blague' in elocution:
                    vocal.say("D'accore, je vais vous faire une blague")
                    vocal.runAndWait()
                    nombre = random.randint(0,49)
                    print(int(nombre))
                    Listeblague = ['40% des accidents sont provoqués par l’alcool… Donc, 60% des accidents sont provoqués par des buveurs d’eau. C’est énorme !','Que faire pour sauver la vie d’une mouche qui se noie ? Du mouche à mouche','C’est l’histoire d’une femme dans le désert qui à l\'air d\'une gourde','C’est l’histoire d’un poil avant il etait bien, maintenant il est pubien','Qu’est-ce qu’on dit quand on appelle un monstre à 4 têtes ? Allo Allo Allo Allo !','Quel est le nom de ma femme de ménage ? Sarah Masse.','Si tu jettes une imprimante dans l’eau… elle a pas pied','Quel fruit le poisson déteste-il le plus ? La pêche.','Qu’est-ce qui est petit, carré et jaune ? Un petit carré jaune!!!','C’est l’histoire d’un chauve, qui a un cheveu sur la langue','Quel mot contient le plus de i ? Simili','Quel est le comble pour une taupe? C’est d’amuser la galerie !','C’est l’histoire d’une fleur qui court, qui court.. Et qui se plante','Que font 2 squelettes le soir de leur mariage ? La nuit de noces','c’est un putois qui rencontre un autre putois et qui lui dit : « Tu pues toi !»','Comment appelle-t-on une blonde qui ne comprends rien à l’informatique ? Une i-conne','Que fait une autruche lorsqu’elle finit de manger du miel ? Elle passe à l’aut’ruche.','Comment appelle-t-on un squelette qui parle ? Un os parleur','Deux puces sortent du cinéma, l’une dit à l’autre : – Tu rentres à pied ? – Oh, non je prends un chien !','Qu’est-ce qu’un chalumeau ?? C\'est un drolumadaire à deux bosse !!','Qu’est-ce qu’un yaourt dans la forêt ? Un yaourt nature','Comment appelle-t-on des rats qui marchent en file indienne ? Une rallonge…','Quel est le comble pour une religieuse ? C’est d’être bonne !','Dans un restaurant, un client dit : – Garçon, que fait cette mouche dans ma soupe ? – Je pense que c’est de la brasse… mais je peux me tromper…','Qu’est-ce qu’un rat avec la queue coupée ? Un rat-courci.','Ce n’est pas parce que 2 chauves discutent, qu’ils sont de mèches !','Quelle est la différence entre le 51 et le 69 ? Le 51 sent l’anis','2 grains de sable dans le désert : – Te retourne pas, mais je crois qu’on est suivi','Pourquoi les oiseaux volent-ils vers le sud ? Car à pied, c’est beaucoup trop long','Pourquoi n’ y a t-il plus de mammouth ? Parce qu’il n’y a plus de papmouth','Un boxeur belge rentre chez lui plein de bleus sur le visage. Sa femme lui demande : – « As-tu gagné ? » - Non, j’ai fini deuxième.''Quel est le jeu préféré des fonctionnaires ? Le Mikado, car c’est le premier qui bouge qui a perdu !','– Papa y’a quelqu’un a la porte avec une moustache. – Dis-lui que j’en ai déjà une.','– Et avec ton mari, çà s’arrange ? – Tu penses… pour l’émoustiller, j’avais mis une nuisette noire et un masque. Quand il est rentré, il m’a fait : Eh ! Zorro ! Qu’est-ce qu’on mange aujourd’hui ?','Comment se reproduisent les hérissons ? En faisant attention.','C’est quoi un morceau de patate qui tombe sur la planète ? Une météofrite','Où se cache Mozart ? Dans le frigo… Car Mozzarella…','Comment est mort le capitaine Crochet ? En se grattant les couilles','C’est quoi une pomme dauphine ? C’est celle qui a fini 2eme à Miss patate','Deux femmes discutent : - Mon mari, il est en or ! – Le mien il est en tôle !','Que dit un rouleau de papier de toilette à Luke Skywalker ? J’éssuie ton père','Comment appelle-t-on un chat tout-terrain ? Un Cat-cat','La fesse gauche à la fesse droite : T’as vu la belle brune qui vient de passer ?','On ne dit pas un ingrat Mais un nain gros.','Si tu vois un oiseau sur un lac… C’est un signe.','Pourquoi les sorcières utilisent des balais pour voler ? Parce que les aspirateurs sont trop lourds !','Chéri, je me sens grosse et laide…S’il te plait, fais-moi un compliment. -Tu as une bonne vue !','C’est un mec qui entre dans un bar et qui dit - Salut c’est moi ! Mais en fait c’était pas lui…','Quand 2 poissons s’énervent.. Est-ce qu’on peut dire que le thon monte ?','Que s’est-il passé en 1111 ? L’invasion des huns.','Au jour de l’an, 2 geeks discutent : -« Qu’est-ce que t’as pris comme résolution cette année ? – 1024 fois 768']
                    vocal.say(Listeblague[nombre])
                    vocal.runAndWait()

                elif 'cherche' in elocution:
                    vocal.say("Je vais faire la recherche pour vous")
                    vocal.runAndWait()
                    elocution = elocution.split(' ')
                    print(elocution)
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
                    vocal.say('Voici les prévision celon Météo France')
                    vocal.runAndWait()
                    webbrowser.open_new('https://meteofrance.com/previsions-meteo-france/nantes/44000')


                #changer les paramêtre du bot
                #elif 'paramètre' in elocution:
                #    vocal.say('Pour changer de mode d\'ouverture des musique dites "musique" + spotify ou youtube.')
                #    vocal.runAndWait()
                #    print("....")
                #    audio = r.listen(source)
                #    elocution = r.recognize_google(audio,language='fr-FR')
                #    elocution=elocution.lower()
                #    print(elocution)
                #    if 'musique' in elocution:
                #        if 'youtube' in elocution:
                #            ModeMusique = 'Youtube'
                #        else:
                #            ModeMusique = 'Spotify'

                    #ignore la phrase qu'elle à enregistrer
                elif 'ignore' in elocution:
                    vocal.say("D'accore maître")
                    vocal.runAndWait()
                elif 'stop'in elocution or 'ferme-la' in elocution or ('ta' in elocution and ' gueule' in elocution):
                    vocal.say("Au revoir Monsieur")
                    vocal.runAndWait()
                    ready = False
                    turtle.bye()
                    quit()
                else:
                    update('Vous avez dit :'+elocution)
                    print("Vous avez dit : " + elocution)
                time.sleep(1)
                update('Appuyer pour parler')
            except:
                update('Je n\'ai pas compris...')
                print("Je n'ai pas compris")
                time.sleep(1)
                update('Appuyer pour parler')




# Ici on fait les test des coordonée de la souris
def click(x, y):
    if x > -250 and x < 250 and y < 250 and y > -250:
        speech()


# onclick action
update("Appuyer pour parler")
wn.onclick(click)
wn.mainloop()