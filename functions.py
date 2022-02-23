from BD import *
from Bibliotheque import *
from Livre import *
from Personne import *
from User import *
from functions import *

###########
# Display #
###########
def clear():
    print("\033[H\033[J", end="")

def menu1():
    clear()
    print("Que voulez-vous faire ?\n"
          "1 - S'identifier\n"
          "2 - Créer un compte\n"
          "3 - Quitter l'application\n")

def menu2():
    print("Que voulez-vous faire ?\n"
          "1 - Afficher emprunts\n"
          "2 - Emprunter\n"
          "3 - Rendre\n"
          "4 - Changer mot de passe\n"
          "5 - Afficher les livres\n"
          "6 - Déconnexion\n")

def classement_maisons(bibliotheque, user):
    clear()
    if user.maison != None:
        print("Classement des quatres Maisons :")
        print(f"\033[31mGryffondor : {bibliotheque.gryffondor_pts}    \033[33mPoufsouffle : {bibliotheque.poufsouffle_pts}    \033[34mSerdaigle : {bibliotheque.serdaigle_pts}  \033[32mSerpentard : {bibliotheque.serpentard_pts}\033[37m\n")

##################
# Gestion erreur #
##################
def check_int(data):
    check = False
    try:
        data = int(data)
    except ValueError:
        print("Entrée incorrect, veuillez rentrer un nombre")
    else:
        check = True
    finally:
        return check

###################
# Check in Classe #
###################
def check_user(bibliotheque, identifiant):
    check = False
    for i in bibliotheque.user_liste:
        if i.id == identifiant:
            check = True
    return check

def check_user_mdp(bibliotheque, identifiant, mdp):
    check = False
    for i in bibliotheque.user_liste:
        if i.id == identifiant and i.mdp == mdp:
            check = True
    return check

def recup_user(bibliotheque, identifiant, mdp):
    for i in bibliotheque.user_liste:
        if i.id == identifiant and i.mdp == mdp:
            return i
