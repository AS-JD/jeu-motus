
from random import *

import time
from tkinter import*	# importation du module tkinter permettant de créer des fenêtre et placer des objets
from tkinter.messagebox import * # boîte de dialogue

def Charger(fichier_mots):
    """Charge le fichier de mots correspondant au nombre de lettres désiré
       dans une liste primaire qui permettra de vérifier si le mot tapé existe,
       et dans une liste secondaire de laquelle il sera retiré pour éviter les répétitions."""
    global listeMots, listeSecondaire,nbrLettres

    fichier = open(fichier_mots,'r')
    listeMots = []
    while 1:
        mot = fichier.readline()
        if mot == "":
            break
        listeMots.append(mot)

    nbrLettres = len(listeMots[0])
    listeSecondaire = listeMots[:]

    fichier.close()

def choix_mot():
    """Sélectionne un mot au hazard dans la liste de mots chargé et
    le retire de la liste secondaire pour éviter les répétitions."""
    global listeSecondaire
    global motA_Trouver
    global coups
    coups = 0
    hazard = randrange(0,len(listeSecondaire))
    motA_Trouver = listeSecondaire[hazard]
    del listeSecondaire[hazard]
    if not listeSecondaire:
        listeSecondaire = listeMots[:]

    return motA_Trouver
def position_lettres(mot_choisi):
    global mot
    global lettres_trouvees
    pl="3333333"
    mot_source=mot_choisi
    mot_copy=mot
    for i in range (7):
        if mot_copy[i]==mot_source[i]:
            pl=pl[:i]+"1"+pl[i+1:]
            lettres_trouvees[i] = mot_copy[i]
            mot_source = mot_source[:i] + "@" + mot_source[i + 1:]
            mot_copy = mot_copy[:i] + "!" + mot_copy[i + 1:]
        if mot_copy[i] in mot_source:
            indice = mot_source.find(mot_copy[i])
            pl=pl[:indice]+"2"+pl[indice+1:]
            mot_source = mot_source[:indice] + "@" + mot_source[indice + 1:]
    return (pl)



def code_couleur(code,prop):

    global coups
    global mot

    lettre=prop
    for i in range(len(lettre)):
        if code[i]=="1":
            e = Label(airDessin, text=lettre[i], background="red", font=(None, 20), foreground='#FFF')
        if code[i]=="2" :
            e = Label(airDessin, text=lettre[i], background="yellow", font=(None, 20), foreground='#FFF')
        if code[i]=="3":
            e = Label(airDessin, text=lettre[i], background="blue", font=(None, 20), foreground='#FFF')
      #implanter votre code ici
        e.grid(row=coups, column=i,columnspan=1, sticky=E+W,ipadx=10,ipady=10,padx=1,pady=1)	# placementment du label texte coloré dans une grille
        fenetre.update()
        time.sleep(.200)
    coups=coups+1

def placer_lettres(coups,lettres,coul):





    d = Label(airDessin, text=lettres[0], background=coul, font=(None, 20), foreground='#FFF')
    d.grid(row=coups, column=0, columnspan=1, sticky=E + W, ipadx=10, ipady=10, padx=1,
            pady=1)  # placementment du label texte coloré dans une grille
    fenetre.update()
    time.sleep(.200)



def Verification():
    global mot
    global coups
    global lettre_trouvees
    choix = Proposition.get().upper()  # récupère la proposition dans le champ entry
    if len(choix) != 7:  # vérifie si le mot contien 7 lettres
        showwarning('Erreur', "le mot ne contient pas 7 lettres")

    else:
        pl = position_lettres(choix)  # récupère la position des lettres
        code_couleur(pl, choix)

        if pl == '1111111' or coups == 6:  # traitement perdu ou gagné
            if pl == "1111111":
                r=askquestion('Résultat', 'Bravo vous avez trouvé  .''\nVoulez-vous recommencer ?')
            else:
                r = askquestion('Résultat', 'Désolé, le mot à trouver était : ' + mot + '.\nVoulez-vous recommencer ?')

            if r == 'no':
                coups=coups-1
                fenetre.quit()
            else:
                coups=0
                init()

        Proposition.set('')
    placer_lettres(coups, mot, 'red')


def init():
    global coups
    global Proposition
    global mot
    mot = choix_mot()
    print (mot)
    label_title = Label(fenetre, text="le jeu de motus ", font=("Script", 40, "bold"), bg='#3A0E44', fg='white')
    label_title2 = Label(fenetre, text="Le jeu du Motus consiste à retrouver un mot de 7 lettres en 6 coups maximum :",
                         font=("Times", 14, "italic"), bg='#3A0E44', fg='white')
    label_title.grid(row=0, column=0)
    label_title2.grid(row=1, column=0)
    for i in range (6):
        for j in range (7):
            c =Label (airDessin,font=(None,20), bg='white',text=".")
            c.grid(row=i, column=j, columnspan=1, sticky=E + W, ipadx=15, ipady=10, padx=1, pady=1)

    airDessin.grid(row=3,column=0)
    fenetre.title('MOTUS')
    fenetre.iconbitmap('imagen-jeu-motus-0big.ico')
    fenetre.config(background='#3A0E44')
    Champ = Entry(airDessin, font=(None, 20), textvariable=Proposition)
    Champ.focus_set()
    Champ.grid(row=9, column=0, columnspan=6, pady=10, padx=10)
    Bouton = Button(airDessin, font=(None, 12), text='Valider', command=Verification,bg='#3A0E44',fg='white')
    Bouton.grid(row=9, column=6, columnspan=2, pady=10, padx=20, sticky=E + W)
    placer_lettres(coups, mot, 'red')


lettres_trouvees=[".",".",".",".",".",".","."]
Charger('mots7.txt')
fenetre = Tk()
airDessin = Frame(fenetre, bg='#3A0E44')
Proposition = StringVar()

init()
fenetre.mainloop()


