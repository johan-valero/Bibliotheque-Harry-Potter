from BD import *
from Bibliotheque import *
from Livre import *
from Personne import *
from User import *
from functions import *

print("------------------------------------------------\n"
      "Bienvenue sur la banque en ligne de la culture !")
input("------------------------------------------------\n")

poney_fringuant = Bibliotheque("poney_fringuant")
poney_fringuant.ImporterLivre()
poney_fringuant.ImporterUser()

# poney_fringuant.AfficherDispo()
# input()

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
                    user_connecte = recup_user(poney_fringuant, identifiant, mdp)
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
                if len(user_connecte.emprunts) == 0:
                    print("Vous n'avez pas d'emprunt en cours\n")
                    input("Entrer pour quitter")
                elif len(user_connecte.emprunts) > 0:
                    user_connecte.AfficherEmprunts(poney_fringuant)
                    print("Souhaitez-vous prolonger un emprunt ? y/n")
                    check_prolongation = input("> ")
                    if check_prolongation == "y":
                        print("Quel emprunt souhaitez-vous prolonger ?")
                        user_connecte.AfficherEmprunts(poney_fringuant)
                        qui_prolonger = input("> ")
                        if check_int(qui_prolonger):
                            qui_prolonger = int(qui_prolonger)
                            if qui_prolonger <= len(user_connecte.emprunts):
                                user_connecte.ProlongerEmprunt(poney_fringuant, user_connecte.emprunts[qui_prolonger - 1])
                                print("Votre demande de prolongation d'emprunt a bien été prise en compte")
                                input()

            # Menu 2 : 2 - Emprunter
            elif choix_menu_2 == "2":
                emprunter = True
                while emprunter:
                    clear()
                    print("Emprunter")
                    print("Vous voulez effectuer une recherche par :\n"
                        "1 - Référence\n"
                        "2 - Titre\n"
                        "3 - Catégorie\n"
                        "4 - Auteur\n"
                        "5 - Genre\n"
                        "6 - Langue\n"
                        "exit pour quitter")
                    choix_recherche = input("> ")
                    
                    if choix_recherche == "exit":
                        input("Abandon recherche")
                        emprunter = False
                    
                    elif choix_recherche == "1":
                        clear()
                        print("Veuillez renseigner la référence recherché :")
                        recherche = input("> ")
                        resultat = poney_fringuant.RechercherLivreParRef(recherche)
                        if resultat.dispo:
                            print("Voulez-vous emprunter :", resultat.titre, "? y/n")
                            check_correct = input("> ")
                            if check_correct == "y":
                                user_connecte.EmprunterLivre(poney_fringuant, resultat)
                                print("Vous avez emprunté", resultat.titre, 
                                    "veuillez le rendre avant le", poney_fringuant.livre_liste[poney_fringuant.RechercheIndex(resultat)].retour)
                                input()
                        else:
                            print(resultat.titre, "n'est pas disponible à l'emprunt")
                            input()

                    elif choix_recherche == "2":
                        clear()
                        print("Veuillez renseigner le titre recherché :")
                        recherche = input("> ")
                        resultat = poney_fringuant.RechercherLivreParTitre(recherche)
                        j = 0
                        for i in resultat:
                            j += 1
                            print(j, "-", i.titre)
                        print("Quel livre voulez-vous emprunter ?")
                        choix_resultat = input("> ")
                        if check_int(choix_resultat):
                            choix_resultat = int(choix_resultat)
                            if choix_resultat <= len(resultat):
                                livre_choisi = resultat[choix_resultat - 1]
                                if livre_choisi.dispo:
                                    user_connecte.EmprunterLivre(poney_fringuant, livre_choisi)
                                    print("Vous avez emprunté", livre_choisi.titre, 
                                        "veuillez le rendre avant le", poney_fringuant.livre_liste[poney_fringuant.RechercheIndex(livre_choisi)].retour)
                                    input()
                                else:
                                    print(livre_choisi.titre, "n'est pas disponible à l'emprunt")
                                    input()
                    
                    elif choix_recherche == "3":
                        clear()
                        print("Veuillez renseigner la catégorie recherchée :")
                        recherche = input("> ")
                        resultat = poney_fringuant.RechercherLivreParCategorie(recherche)
                        j = 0
                        for i in resultat:
                            j += 1
                            print(j, "-", i.titre)
                        print("Quel livre voulez-vous emprunter ?")
                        choix_resultat = input("> ")
                        if check_int(choix_resultat):
                            choix_resultat = int(choix_resultat)
                            if choix_resultat <= len(resultat):
                                livre_choisi = resultat[choix_resultat - 1]
                                if livre_choisi.dispo:
                                    user_connecte.EmprunterLivre(poney_fringuant, livre_choisi)
                                    print("Vous avez emprunté", livre_choisi.titre, 
                                        "veuillez le rendre avant le", poney_fringuant.livre_liste[poney_fringuant.RechercheIndex(livre_choisi)].retour)
                                    input()
                                else:
                                    print(livre_choisi.titre, "n'est pas disponible à l'emprunt")
                                    input()
                    
                    elif choix_recherche == "4":
                        clear()
                        print("Veuillez renseigner l'auteur recherché :")
                        recherche = input("> ")
                        resultat = poney_fringuant.RechercherLivreParAuteur(recherche)
                        j = 0
                        for i in resultat:
                            j += 1
                            print(j, "-", i.titre)
                        print("Quel livre voulez-vous emprunter ?")
                        choix_resultat = input("> ")
                        if check_int(choix_resultat):
                            choix_resultat = int(choix_resultat)
                            if choix_resultat <= len(resultat):
                                livre_choisi = resultat[choix_resultat - 1]
                                if livre_choisi.dispo:
                                    user_connecte.EmprunterLivre(poney_fringuant, livre_choisi)
                                    print("Vous avez emprunté", livre_choisi.titre, 
                                        "veuillez le rendre avant le", poney_fringuant.livre_liste[poney_fringuant.RechercheIndex(livre_choisi)].retour)
                                    input()
                                else:
                                    print(livre_choisi.titre, "n'est pas disponible à l'emprunt")
                                    input()
                    
                    elif choix_recherche == "5":
                        clear()
                        print("Veuillez renseigner le genre recherché :")
                        recherche = input("> ")
                        resultat = poney_fringuant.RechercherLivreParGenre(recherche)
                        j = 0
                        for i in resultat:
                            j += 1
                            print(j, "-", i.titre)
                        print("Quel livre voulez-vous emprunter ?")
                        choix_resultat = input("> ")
                        if check_int(choix_resultat):
                            choix_resultat = int(choix_resultat)
                            if choix_resultat <= len(resultat):
                                livre_choisi = resultat[choix_resultat - 1]
                                if livre_choisi.dispo:
                                    user_connecte.EmprunterLivre(poney_fringuant, livre_choisi)
                                    print("Vous avez emprunté", livre_choisi.titre, 
                                        "veuillez le rendre avant le", poney_fringuant.livre_liste[poney_fringuant.RechercheIndex(livre_choisi)].retour)
                                    input()
                                else:
                                    print(livre_choisi.titre, "n'est pas disponible à l'emprunt")
                                    input()
                    
                    elif choix_recherche == "6":
                        clear()
                        print("Veuillez renseigner la langue recherchée :")
                        recherche = input("> ")
                        resultat = poney_fringuant.RechercherLivreParLangue(recherche)
                        j = 0
                        for i in resultat:
                            j += 1
                            print(j, "-", i.titre)
                        print("Quel livre voulez-vous emprunter ?")
                        choix_resultat = input("> ")
                        if check_int(choix_resultat):
                            choix_resultat = int(choix_resultat)
                            if choix_resultat <= len(resultat):
                                livre_choisi = resultat[choix_resultat - 1]
                                if livre_choisi.dispo:
                                    user_connecte.EmprunterLivre(poney_fringuant, livre_choisi)
                                    print("Vous avez emprunté", livre_choisi.titre, 
                                        "veuillez le rendre avant le", poney_fringuant.livre_liste[poney_fringuant.RechercheIndex(livre_choisi)].retour)
                                    input()
                                else:
                                    print(livre_choisi.titre, "n'est pas disponible à l'emprunt")
                                    input()

            # Menu 3 : 3 - Rendre
            elif choix_menu_2 == "3":
                clear()
                print("Rendre")
                if len(user_connecte.emprunts) == 0:
                    input("Vous n'avez pas d'emprunts en cours")
                else:
                    j = 0
                    for i in user_connecte.emprunts:
                        j += 1
                        print(j, "-", i.titre, "\n")

                    livre_a_rendre = input("Quel livre désirez-vous rendre ? \"exit\" pour quitter\n> ")
                    while not check_int(livre_a_rendre):
                        if livre_a_rendre == "exit":
                            break
                        else:
                            print("Je n'ai pas compris")
                            livre_a_rendre = input("Quel livre désirez-vous rendre ?\n\"exit\" pour quitter\n> ")
                
                    if livre_a_rendre != "exit":
                        livre_a_rendre = int(livre_a_rendre) - 1
                        user_connecte.RendreLivre(poney_fringuant, user_connecte.emprunts[livre_a_rendre])
                        input("Vous avez rendu votre livre")


            # Menu 4 : 4 - Changer mot de passe
            elif choix_menu_2 == "4":
                # check sécurité
                clear()
                print("Changement de mot de passe\n")
                check_secu = input("Veuillez rentrer votre mot de passe :\n> ")
                if check_user_mdp(poney_fringuant, user_connecte.nom, check_secu):
                    new_mdp = input("Veuillez renseigner le nouveau mot de passe :\n> ")
                    check_new_mdp = input("Veuillez confirmer le nouveau mot de passe :\n> ")
                    if new_mdp == check_new_mdp:
                        user_connecte.ChangerMdp(new_mdp)
                        input("Votre mot de passe a été changé avec succés")
                    
                    elif new_mdp != check_new_mdp:
                        input("Erreur, abandon du changement de mot de passe")
                
                elif not check_user_mdp(poney_fringuant, user_connecte.nom, check_secu):
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
        poney_fringuant.user_liste.append(user)
        input("Votre compte a été crée avec succès !")

    # Menu 1 : 3 - quitter Application
    elif choix_menu_1 == "3":
        # poney_fringuant.ExporterLivre() # -> Corriger ExporterLivre (all livres et pas que un)
        # poney_fringuant.ExporterUser() # -> Pareil qu'au dessus
        input("Bonne journée !")
        break
