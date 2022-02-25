from Bibliotheque import *

# ! Revoir les imports fichiers de tous les fichiers pour supprimer redondance clear() et check(int)
# ! Finir de factoriser le main.py : displays, start et exit, Emprunter, Rechercher doivent être déplacés
# TODO: Revoir repr de toutes les classes

# TODO: créer fonction display_start() dans function.py qui affiche l'ASCII

print("------------------------------------------------\n"
      "Bienvenue sur la bibliothèque de Poudlard !")
print('''                                                                                                           
                                                   @                                      
                                                   @                                      
                                                   @                                     
                                                  @@@                                     
                             (                   @@@@@                                    
                             (                   @@@@@                                    
                             /                  @@@@@@@                                   
                             @                  @@@@@@@                                   
                            @@@            @   @@@@@@@@@   /                              
                           @@@@@           @    @@@@@@@    @                              
                          @@@@@@@          @@   @@@ @@@    @                             
                           @   @          @@@@  @@@@@@@   @@@                             
                          @@@@@@@        @@@@@@ @@@@@@@  @@@@                             
                        @@@@@@@@@@@      @@@@@  @@@@@@@@@@@@@@                            
                        @@@@@@@@@@@      @@@@@  @@@@@@@@@@@@@@                            
     /                   @@@@@@@@@       @@@@@@@@@@@@@@@@@@@@@                            
     @                   @@@@@@@@@       @@@@@@@@@@@@@@@@@@@@@                            
     @                   @@@@@@@@@       @@@@@@@@@@@@@@@@@@@@@        .                   
    @@@                  @@@@@@@@@       @@@@@@@@@@@@@@@@@@@@@       @@                   
   @@@@@    @            @@@@@@@@@       @@@@@@@@@@@@@@@@@@@@@@     @@@@                  
  @@@@@@    @            @@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@     @@@@                  
  @@@@@    @@@           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
  @@@@@@@ @@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
 @@@@@@@@ @@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
 @@@@@@@@ @@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       @      
 @@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@     
  @@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@    @@@@@@@   
  @@@@@@@@@@@@@  @@@  @@@ @@@ @@@@ @@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@  
  @@@@@@@@@@@@@  @@@  @@@ @@@ @@@@ @@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@  
  @@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@
''')      
input("------------------------------------------------\n")

# TODO: Créer fonction start() pour tous les imports présent et futur du start

hogwarts_library = Bibliotheque("hogwarts_library")
hogwarts_library.ImporterLivre()
hogwarts_library.ImporterUser()
hogwarts_library.ImportClassement()

# TODO: Ajouter connexion possible après la création d'un compte

while True:
    # ###### #
    # Menu 1 #
    # ###### ############################
    menu1()                             #
    choix_menu_1 = input("> ")          #
    # ###################################
    
# TODO: Déplacer identification dans méthode de classe (voir laquelle)

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
            
# ! attention pb secu, possibilité de déduire l'existence d'un compte

            if check_user(hogwarts_library, identifiant):
                mdp = input("Veuillez rentrer votre mot de passe :\n> ")
                if check_user_mdp(hogwarts_library, identifiant, mdp):
                    clear()
                    print("-------------------\n"
                          "Connexion réussie !")
                    input("-------------------")
                    connexion = True
                    identification = False
                    user_connecte = recup_user(hogwarts_library, identifiant, mdp)
                    break
                
                elif not check_user_mdp(hogwarts_library, identifiant, mdp):
                    print("Erreur, veuillez réessayer")
                    identification = False
                    break

        while connexion:
            # ###### #
            # Menu 2 #
            # ###### #################################################
            classement_maisons(hogwarts_library, user_connecte)       #
            menu2()                                                  #
            choix_menu_2 = input("> ")                               #
            # ########################################################

            # Menu 2 : 1 - Afficher emprunts
            if choix_menu_2 == "1":
                user_connecte.AfficherEmprunts(hogwarts_library)

# TODO: Déplacer Emprunter dans classe User
# TODO: Ajout regex + lowercase + str in chaineStr pour élargir résultat recherche
# TODO: Mettre en place une meilleure visibilité de la diponibilité d'un livre (couleur)

        # Ajouter menu 1.2 Classement des maisons
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
                        resultat = hogwarts_library.RechercherLivreParRef(recherche)
                    
                        if resultat != None:
                            if resultat.dispo:
                                print("Voulez-vous emprunter :", resultat.titre, "? y/n")
                                check_correct = input("> ")
                                if check_correct == "y":
                                    user_connecte.EmprunterLivre(hogwarts_library, resultat)
                                    input()
                            else:
                                print(resultat.titre, "n'est pas disponible à l'emprunt")
                                input()
                        else:
                            print("Pas de livre enregistré à cette référence")
                            input("> ")

                    elif choix_recherche == "2":
                        clear()
                        print("Veuillez renseigner le titre recherché :")
                        recherche = input("> ")
                        resultat = hogwarts_library.RechercherLivreParTitre(recherche)
                        j = 0
                        for i in resultat:
                            j += 1
                            print(j, "-", i.titre)
                        choix_resultat = input("> ")
                        if check_int(choix_resultat):
                            choix_resultat = int(choix_resultat)
                            if choix_resultat <= len(resultat):
                                livre_choisi = resultat[choix_resultat - 1]
                                if livre_choisi.dispo:
                                    user_connecte.EmprunterLivre(hogwarts_library, livre_choisi)
                                    input()
                                else:
                                    print(livre_choisi.titre, "n'est pas disponible à l'emprunt")
                                    input()
                    
                    elif choix_recherche == "3":
                        clear()
                        print("Veuillez renseigner la catégorie recherchée :")
                        recherche = input("> ")
                        resultat = hogwarts_library.RechercherLivreParCategorie(recherche)
                        j = 0
                        for i in resultat:
                            j += 1
                            print(j, "-", i.titre)
                        choix_resultat = input("> ")
                        if check_int(choix_resultat):
                            choix_resultat = int(choix_resultat)
                            if choix_resultat <= len(resultat):
                                livre_choisi = resultat[choix_resultat - 1]
                                if livre_choisi.dispo:
                                    user_connecte.EmprunterLivre(hogwarts_library, livre_choisi)
                                    input()
                                else:
                                    print(livre_choisi.titre, "n'est pas disponible à l'emprunt")
                                    input()
                    
                    elif choix_recherche == "4":
                        clear()
                        print("Veuillez renseigner l'auteur recherché :")
                        recherche = input("> ")
                        resultat = hogwarts_library.RechercherLivreParAuteur(recherche)
                        j = 0
                        for i in resultat:
                            j += 1
                            print(j, "-", i.titre)
                        choix_resultat = input("> ")
                        if check_int(choix_resultat):
                            choix_resultat = int(choix_resultat)
                            if choix_resultat <= len(resultat):
                                livre_choisi = resultat[choix_resultat - 1]
                                if livre_choisi.dispo:
                                    user_connecte.EmprunterLivre(hogwarts_library, livre_choisi)
                                    input()
                                else:
                                    print(livre_choisi.titre, "n'est pas disponible à l'emprunt")
                                    input()
                    
                    elif choix_recherche == "5":
                        clear()
                        print("Veuillez renseigner le genre recherché :")
                        recherche = input("> ")
                        resultat = hogwarts_library.RechercherLivreParGenre(recherche)
                        j = 0
                        for i in resultat:
                            j += 1
                            print(j, "-", i.titre)
                        choix_resultat = input("> ")
                        if check_int(choix_resultat):
                            choix_resultat = int(choix_resultat)
                            if choix_resultat <= len(resultat):
                                livre_choisi = resultat[choix_resultat - 1]
                                if livre_choisi.dispo:
                                    user_connecte.EmprunterLivre(hogwarts_library, livre_choisi)
                                    input()
                                else:
                                    print(livre_choisi.titre, "n'est pas disponible à l'emprunt")
                                    input()
                    
                    elif choix_recherche == "6":
                        clear()
                        print("Veuillez renseigner la langue recherchée :")
                        recherche = input("> ")
                        resultat = hogwarts_library.RechercherLivreParLangue(recherche)
                        j = 0
                        for i in resultat:
                            j += 1
                            print(j, "-", i.titre)
                        choix_resultat = input("> ")
                        if check_int(choix_resultat):
                            choix_resultat = int(choix_resultat)
                            if choix_resultat <= len(resultat):
                                livre_choisi = resultat[choix_resultat - 1]
                                if livre_choisi.dispo:
                                    user_connecte.EmprunterLivre(hogwarts_library, livre_choisi)
                                    input()
                                else:
                                    print(livre_choisi.titre, "n'est pas disponible à l'emprunt")
                                    input()

            # Menu 3 : 3 - Rendre
            elif choix_menu_2 == "3":
                user_connecte.RendreLivre(hogwarts_library)

            # Menu 4 : 4 - Changer mot de passe
            elif choix_menu_2 == "4":
                user_connecte.ChangerMdp()

            #Menu 5 : 5 - Afficher les livres
            elif choix_menu_2 == "5":
                hogwarts_library.AfficherLivresTotaux()
                input("> ")

            # Menu 5 : 5 - Déconnexion
            elif choix_menu_2 == "6":
                clear()
                input("Déconnexion réussie")
                connexion = False

# TODO: Déplacer inscription dans classe Bibliotheque

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
        hogwarts_library.user_liste.append(user)
        input("Votre compte a été crée avec succès !")
        print("N'oubliez pas vos identifiants :", user.id)
        input()

# TODO: Créer fonction exit() pour tout les exports présents et futur du exit()
# TODO: Déplacer Dobby dans une fonction display_dobby()

    # Menu 1 : 3 - quitter Application
    elif choix_menu_1 == "3":
        hogwarts_library.ExporterLivre()
        hogwarts_library.ExporterUser()
        hogwarts_library.ExporterClassement()
        input("Bonne journée !")
        print(''' 
   _____
  /     |
/- (*) (*)
|/\.  _>/\|
    \__/   \/
   _| |_   \-/
  /|\__|\  //
 |/|   |\\//
 |||   | ~'
 ||| __|
 /_\| ||
 \_/| ||
   |7 |7
   || ||
   || ||
   /\ \ \ 
  ^^^^ ^^^ ''')

        break
