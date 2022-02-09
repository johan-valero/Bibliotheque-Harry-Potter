import datetime
from Personne import Personne
from Livre import *
from datetime import date, timedelta

class User(Personne):
    def __init__(self, nom, prenom, mdp):
        super().__init__(nom, prenom, mdp)
        self.emprunts = []
        self.grade = "Moldu"
        self.compteur_livre = 0
        self.maison = None
    
    def __repr__(self):
        return str(f"[{self.nom}, {self.prenom}, {self.mdp}, {self.emprunts}, {self.grade}, {self.compteur_livre}, {self.maison}]")
    
    # Utilities
    def Check_int(self, data):
        check = False
        try:
            data = int(data)
        except ValueError:
            print("Entrée incorrect, veuillez rentrer un nombre")
        else:
            check = True
        finally:
            return check
    
    def Clear(self):
        print("\033[H\033[J", end="")

    # Afficher Emprunts + Prolonger
    def ListeEmpruntsNum(self, bibliotheque):
        j = 0
        for i in self.emprunts:
            j += 1
            print(j, "-", bibliotheque.livre_liste[bibliotheque.RechercheIndexParRef(i)].titre, "à rendre avant le", bibliotheque.livre_liste[bibliotheque.RechercheIndexParRef(i)].retour)
    
    def ProlongerEmprunt(self, bibliotheque, livre_ref):
        dateRetour = bibliotheque.livre_liste[bibliotheque.RechercheIndexParRef(livre_ref)].retour 
        dateRetour += timedelta(days=7)
        bibliotheque.livre_liste[bibliotheque.RechercheIndexParRef(livre_ref)].retour = dateRetour
    
    def AfficherEmprunts(self, bibliotheque):
        self.Clear()
        print("Emprunts\n")
        if len(self.emprunts) == 0:
            print("Vous n'avez pas d'emprunt en cours\n")
            input("Entrer pour quitter")
        
        elif len(self.emprunts) > 0:
            print("Vous avez", len(self.emprunts), "emprunt(s) en cours :")
            self.ListeEmpruntsNum(bibliotheque)
            print("Souhaitez-vous prolonger un emprunt ? y/n")
            check_prolongation = input("> ")
            
            if check_prolongation == "y":
                print("Quel emprunt souhaitez-vous prolonger ?")
                self.ListeEmpruntsNum(bibliotheque)
                qui_prolonger = input("> ")
                
                if self.Check_int(qui_prolonger):
                    qui_prolonger = int(qui_prolonger)
                    if qui_prolonger <= len(self.emprunts):
                        self.ProlongerEmprunt(bibliotheque, self.emprunts[qui_prolonger - 1])
                        print("Votre demande de prolongation d'emprunt a bien été prise en compte")
                        input()

    # Emprunter un livre + Rendre un livre
    def ChoisirMaison(self):
        self.Clear()
        print('''                                    
                                           &&&&&&&&&&&&&%                                 
                                         &&&.*&&&/&&&&&&&&&&&&&&@*                        
                                        %&&&&/ &&.&&&&&&&&&&&&&&&&&&&*                    
                                       ,&&&&&&  @. *&&&&&((((/,,,..                       
                                       @&&&&&&&%  &   &&&,                                
                                   ,@&&&&&&&&&&&&&&&%/&%                                  
                                  @&&&&&&&&&&&&&&&&&&&                                    
                                 #&&&&&&&&&&&&&&&&&&&&&,                                  
                                 &&&&&&&&&&&&&&&&&&&&&&&,                                 
                               %&&&&&&&&&&&&&&&&&&&&&&&&&/                                
                             &&&&&&&*     *&&&&&&&&&&&&&&&%                               
                            ,&&&&&&&&,       &&&&&&&&&&&&&&&.                             
                             @&&&&&&&&@        &&&&&&&&&&/ /                              
                             ,&&&&&&&&&&%        %&&&(     @                              
                              &&&&&&&&&&&&&@#*          *&&&&                             
                             #&&&&&&&&&&&&&%  &&&&&&&&% (&&&&&                            
                            ,&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&,                          
                            @&&&&&&&&&&&&&&&&&%/.          *&&&&#                         
                           &&&&&&&&&&&&&@(                   (&,&&                        
                         &&&&&&&&&&&@.      ,(%&&&&&&&&&&&&&&&&* (&#                      
                        .&&,&&&@,  %&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&       %@&&&&&&&&@   
                         @&&,*@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&/        %&  
                         (&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%.            ,&/  
                         %&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@*          ,%&&@(.      
     #&&&&&&&&&&&&@@&&@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@     **@@@&%.               
  &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#,                                 
 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@%*                                          
   .@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@%*                                                  
            ,(@@@@@@@@@@((.''')
        print("Mais vous avez des pouvoirs magiques ?!\n"
              "Vos lectures vous ont permi de devenir Apprenti Sorcier !\n"
              "En tant que tel, vous vous devez de choisir une maison !")
        input()
        continuer = True
        while continuer:
            print("Quelle maison vous intéresse ?")
            # Affichage des ASCII Blason
            choix_maison = input("> ")
            if choix_maison == "1":
                self.Clear()
                input("Gryffondor")
            elif choix_maison == "2":
                self.Clear()
                input("Poufsouffle")
            elif choix_maison == "3":
                self.Clear()
                input("Serdaigle")
            elif choix_maison == "4":
                self.Clear()
                input("Serpentard")
            elif choix_maison == "5":
                self.Clear()
                print("Entrez votre choix final en toute lettre pour prêter allégeance à votre maison")
                maison_choisie = input("> ")
                while not maison_choisie == "Griffondor" and not maison_choisie == "Poufsouffle" and not maison_choisie == "Serdaigle" and not maison_choisie == "Serpentard":
                    maison_choisie = input("> ")
                print("Vous avez choisi :", maison_choisie, ", confirmer ? y/n")
                print("\033[31mAttention ce choix est définitif !\033[37m")
                confirmation = input("> ")
                if confirmation == "y":
                    self.maison = maison_choisie
                    print("Vous défendrez donc les couleurs de", maison_choisie, "!")
                    input("Vous avez désormais accée au Classement des Maisons, que la meilleure gagne !")
                    continuer = False
                else:
                    input("Je vois que vous hésitez encore, prenez le temps d'y réfléchir")
        
    
    def Grade(self):
        if self.compteur_livre == 5 and self.grade == "Moldu":
            self.grade = "Apprenti Sorcier"
            self.ChoisirMaison()

        elif self.compteur_livre == 10 and self.grade == "Apprenti Sorcier":
            self.grade = "Sorcier"

        elif self.compteur_livre == 40 and self.grade == "Sorcier":
            self.grade = "Auror"
    
    # Emprunter
    def EmprunterLivre(self, bibliotheque, livre):
        dico_grade = {"Moldu": 1, "Apprenti sorcier": 2, "Sorcier": 3, "Auror": 4}
        for i in dico_grade:
            if self.grade == i:
                nb_max_emprunts = dico_grade[i]
        
        if len(self.emprunts) == nb_max_emprunts:
            input("Vous ne pouvez pas emprunter de livre en plus")
        
        elif len(self.emprunts) < nb_max_emprunts:
            dateDuJour = date.today()
            tempsEmprunt = timedelta(days=7)
            dateRetour = dateDuJour + tempsEmprunt
            bibliotheque.livre_liste[bibliotheque.RechercheIndexParLivre(livre)].dispo = False
            bibliotheque.livre_liste[bibliotheque.RechercheIndexParLivre(livre)].retour = dateRetour
            
            self.emprunts.append(livre.ref)
    
    # Rendre
    def RendreLivre(self, bibliotheque):
        self.Clear()
        print("Rendre")
        if len(self.emprunts) == 0:
            input("Vous n'avez pas d'emprunts en cours")
        else:
            j = 0
            for i in self.emprunts:
                j += 1
                print(j, "-", bibliotheque.livre_liste[bibliotheque.RechercheIndexParRef(i)].titre, "\n")

            choix_livre_a_rendre = input("Quel livre désirez-vous rendre ? \"exit\" pour quitter\n> ")
            while not self.Check_int(choix_livre_a_rendre):
                if choix_livre_a_rendre == "exit":
                    break
                else:
                    print("Je n'ai pas compris")
                    choix_livre_a_rendre = input("Quel livre désirez-vous rendre ?\n\"exit\" pour quitter\n> ")
                
            if choix_livre_a_rendre != "exit":
                choix_livre_a_rendre = int(choix_livre_a_rendre) - 1
                livre_a_rendre = self.emprunts[choix_livre_a_rendre]

                bibliotheque.livre_liste[bibliotheque.RechercheIndexParRef(livre_a_rendre)].dispo = True
                bibliotheque.livre_liste[bibliotheque.RechercheIndexParRef(livre_a_rendre)].retour = None
                self.compteur_livre += 1
                self.emprunts.remove(livre_a_rendre)
                input("Vous avez rendu votre livre")
                self.Grade()

    # Changer Mdp
    def Check_mdp(self, mdp):
        check = False
        if self.mdp == mdp:
                check = True
        return check
    
    def ChangerMdp(self):
        self.Clear()
        print("Changement de mot de passe\n")
        check_secu = input("Veuillez rentrer votre mot de passe :\n> ")
        if self.Check_mdp(check_secu):
            new_mdp = input("Veuillez renseigner le nouveau mot de passe :\n> ")
            while len(new_mdp) < 5:
                print("Votre nouveau mot de passe n'est pas assez long (5 caractères minimums)")
                new_mdp = input("Veuillez renseigner le nouveau mot de passe :\n> ")
            
            check_new_mdp = input("Veuillez confirmer le nouveau mot de passe :\n> ")
            if new_mdp == check_new_mdp:
                self.mdp = new_mdp
                input("Votre mot de passe a été changé avec succés")
                    
            elif new_mdp != check_new_mdp:
                input("Erreur, abandon du changement de mot de passe")
                
        elif not self.Check_mdp(check_secu):
            input("Erreur, abandon du changement de mot de passe")
