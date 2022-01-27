from BD import *
from Bibliotheque import *
from Livre import *
from Personne import *
from User import *
from functions import *

print("------------------------------------------------\n"
      "Bienvenue sur la banque en ligne de la culture !")
input("------------------------------------------------\n")

while True:
    # ###### #
    # Menu 1 #
    # ###### ############################
    menu1()                             #
    choix_menu_1 = input()              #
    # ###################################
    
    # Menu 1 : identification
    if choix_menu_1 == "1":
        clear()
        print("---------\n"
              "Connexion\n"
              "---------")
        identifiant = input("Veuillez entrer vos identifiants ou \"exit\" pour quitter\n")
        if check_user(identifiant):
            mdp = input("Veuillez rentrer votre mot de passe :\n")
            if check_user_mdp(identifiant, mdp):
                clear()
                print("-------------------\n"
                      "Connexion réussie !")
                input("-------------------")
                connexion = True
                while connexion:
                    # ###### #
                    # Menu 2 #
                    # ###### ################
                    menu2()                 #
                    choix_menu_2 = input()  #
                    # #######################

                    # Menu 2 : Afficher emprunts
                    if choix_menu_2 == "1":
                        # #
                        # # -> user.emprunt_liste
                        # #
                        clear()
                        print("Emprunts\n")
                        if len(identifiant.emprunt_liste) == 0:
                            input("Vous n'avez pas d'emprunt en cours")

                    # Menu 2 : Emprunter
                    elif choix_menu_2 == "2":
                        clear()
                        print("Emprunter")
                        # #
                        # # -> RechercherLivre
                        # #
                        # # -> Choisir Livre
                        # #
                        # # -> EmprunterLivre
                        # #

                    # Menu 3 : Rendre
                    elif choix_menu_2 == "3":
                        clear()
                        print("Rendre")
                        # #
                        # # -> RendreLivre
                        # #

                    # Menu 4 : Changer mot de passe
                    elif choix_menu_2 == "4":
                        # check sécurité
                        clear()
                        print("Changement de mot de passe\n")
                        check_secu = input("Veuillez rentrer votre mot de passe :\n")
                        if check_user_mdp(identifiant, check_secu):
                            new_mdp = input("Veuillez renseigner le nouveau mot de passe :\n")
                            check_new_mdp = input("Veuillez confirmer le nouveau mot de passe :\n")
                            if new_mdp == check_new_mdp:
                                # #
                                # # -> user.mdp = new_mdp
                                # #
                                input("Votre mot de passe a été changé avec succés")
                            elif new_mdp != check_new_mdp:
                                input("Erreur, abandon du changement de mot de passe")
                        elif not check_user_mdp(identifiant, check_secu):
                            input("Erreur, abandon du changement de mot de passe")

                    # Menu 5 : Déconnexion
                    elif choix_menu_2 == "5":
                        clear()
                        input("Déconnexion réussie")
                        connexion = False

            elif not check_user_mdp(identifiant, mdp):
                print("Erreur, veuillez réessayer")

        # Quitter identification
        elif identifiant == "exit":
            choix_menu_1 = ""
        
        # Erreur
        else:
            print("Erreur, veuillez réessayer")

    # Menu 1 : inscription
    elif choix_menu_1 == "2":
        print("-----------\n"
              "Inscription\n"
              "-----------\n")
              # #
              # # -> Faire inscription
              # #
        

    # Menu 1 : quitter Application
    elif choix_menu_1 == "3":
        # #
        # # -> Export Livre vers txt
        # #
        # # -> Export User vers txt
        # #
        input("Bonne journée !")
        break