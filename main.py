from BD import *
from Bibliotheque import *
from Livre import *
from Personne import *
from User import *
from functions import *

print("------------------------------------------------\n"
      "Bienvenue sur la banque en ligne de la culture !")
input("------------------------------------------------\n")

poney_fringuant =  Bibliotheque("poney_fringuant")
poney_fringuant.ImporterLivre()
poney_fringuant.ImporterUsers()

while True:
    # ###### #
    # Menu 1 #
    # ###### ############################
    menu1()                             #
    choix_menu_1 = input("> ")          #
    # ###################################
    
    # Menu 1 : 1 - identification
    if choix_menu_1 == "1":
        identification = True
        connexion = False
        while identification:
            clear()
            print("---------\n"
                  "Connexion\n"
                  "---------")
            identifiant = input("Veuillez entrer vos identifiants ou \"exit\" pour quitter\n> ")
            
            # Quitter identification
            if identifiant == "exit":
                identification = False
                break
            
            if check_user(poney_fringuant, identifiant):
                mdp = input("Veuillez rentrer votre mot de passe :\n> ")
                if check_user_mdp(poney_fringuant, identifiant, mdp):
                    clear()
                    print("-------------------\n"
                          "Connexion réussie !")
                    input("-------------------")
                    connexion = True
                    identification = False
                    break
                
                elif not check_user_mdp(poney_fringuant, identifiant, mdp):
                    print("Erreur, veuillez réessayer")
                    identification = False
                    break

        while connexion:
            # ###### #
            # Menu 2 #
            # ###### ###################
            menu2()                    #
            choix_menu_2 = input("> ") #
            # ##########################

            # Menu 2 : 1 - Afficher emprunts
            if choix_menu_2 == "1":
                clear()
                print("Emprunts\n")
                if len(identifiant.emprunt_liste) == 0:
                    print("Vous n'avez pas d'emprunt en cours")
                    input("Entrer pour quitter")
                elif len(identifiant.emprunt_liste) > 0:
                    identifiant.AfficherEmprunt()
                    input("Entrer pour quitter")

            # Menu 2 : 2 - Emprunter
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

            # Menu 3 : 3 - Rendre
            elif choix_menu_2 == "3":
                clear()
                print("Rendre")
                j = 0
                for i in identifiant.liste_emprunt:
                    j += 1
                    print(j, "-", i.nom, "\n")

                livre_a_rendre = input("Quel livre désirez-vous rendre ? \"exit\" pour quitter\n> ")
                while not check_int(livre_a_rendre):
                    if livre_a_rendre == "exit":
                        break
                    else:
                        print("Je n'ai pas compris")
                        livre_a_rendre = input("Quel livre désirez-vous rendre ?\n\"exit\" pour quitter\n> ")
            
                if livre_a_rendre != "exit":
                    livre_a_rendre = int(livre_a_rendre) - 1
                    identifiant.Rendre(identifiant.liste_emprunt[livre_a_rendre])
                    input("Vous avez rendu votre livre")


            # Menu 4 : 4 - Changer mot de passe
            elif choix_menu_2 == "4":
                # check sécurité
                clear()
                print("Changement de mot de passe\n")
                check_secu = input("Veuillez rentrer votre mot de passe :\n> ")
                if check_user_mdp(identifiant, check_secu):
                    new_mdp = input("Veuillez renseigner le nouveau mot de passe :\n> ")
                    check_new_mdp = input("Veuillez confirmer le nouveau mot de passe :\n> ")
                    if new_mdp == check_new_mdp:
                        identifiant.ChangerMdp(new_mdp)
                        input("Votre mot de passe a été changé avec succés")
                    
                    elif new_mdp != check_new_mdp:
                        input("Erreur, abandon du changement de mot de passe")
                
                elif not check_user_mdp(identifiant, check_secu):
                    input("Erreur, abandon du changement de mot de passe")

            # Menu 5 : 5 - Déconnexion
            elif choix_menu_2 == "5":
                clear()
                input("Déconnexion réussie")
                connexion = False

    # Menu 1 : 2 - inscription
    elif choix_menu_1 == "2":
        clear()
        print("-----------\n"
              "Inscription\n"
              "-----------\n")
        nom = input("Veuillez renseigner votre nom\n> ")
        prenom = input("Veuillez renseigner votre prénom\n> ")
        mdp = input("Veuillez renseigner votre mot de passe\n> ")
        while len(mdp) < 5:
            print("Votre mot de passe est trop court, veuillez entrer un mot de passe de minimum 5 caractères.")
            mdp = input("> ")
        user = User(nom, prenom, mdp)
        input("Votre compte a été crée avec succès !")

    # Menu 1 : 3 - quitter Application
    elif choix_menu_1 == "3":
        poney_fringuant.ExporterLivre()
        poney_fringuant.ExporterUser()
        input("Bonne journée !")
        break
