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

# TODO: Ajouter display_start()

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

# TODO: Ajouter fonction display qui prend en paramètre une liste pour gèrer l'affichage d'un grand nombre de données (liste_livre notament)
# TODO: L'idée c'est de ranger les objets de la liste dans d'autre listes (à taille prédéfinie)
# TODO: Avec ces nouvelles listes, on veut en afficher un certain nombre en colonnes
# TODO: Il faudra destructurer les infos des objets pour pouvoir les afficher sur 3-4 colonnes
# TODO: comprendre les mêmes attributs de 3-4 objets dans la même liste
# TODO: d'où l'intérêt des tailles prédéfinies pour éviter des décallages ^^
# TODO: Prévoir une gestion des données trop longues pour les afficher en fin de liste
# TODO: Prévoir également un isinstance pour séparer dès le départ les livres des bd et par la suite le reste de la médiathèque
# TODO: Ne pas oublier d'ajouter la possibilité de "exit" l'affichage à tout moment
# TODO: Déterminer le nombre de page pour que l'utilisateur sache où il en est
# TODO: Si possible ajouter une navigation au sein de ces pages (surement avec un compteur pour aller chercher l'index à afficher)
# ! Si quelqu'un est chaud de se pencher la-dessus pour mettre ça en place
# ! Un petit récap de ce qu'il faudra utiliser :
# !                 des boucles (vous n'y échapperez pas xD)
# !                 isinstance (le fameux)
# !                 len(list)
# !                 l'ajout de plusieurs entrée remplies d'espaces entre chaque entrées de la liste pour homogénéiser l'affichage entres-elles

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

###################################
# Check in Classe pour connection #
###################################
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
