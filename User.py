import datetime
from Personne import Personne
from Livre import *
from datetime import date, timedelta

class User(Personne):
    def __init__(self, nom, prenom, mdp):
        super().__init__(nom, prenom, mdp)
        self.emprunts = []
        self.grade = "gollum"
        self.compteurLivre = 0
    
    def __repr__(self):
        return str(f"[{self.nom}, {self.prenom}, {self.mdp}, {self.emprunts}, {self.grade}]")

    def AfficherEmprunts(self, bibliotheque):
        print("Vous avez", len(self.emprunts), "emprunt(s) en cours :")
        j = 0
        for i in self.emprunts:
            j += 1
            print(j, "-", bibliotheque.livre_liste[bibliotheque.RechercheIndexParRef(i)].titre, "à rendre avant le", bibliotheque.livre_liste[bibliotheque.RechercheIndexParRef(i)].retour)

    def EmprunterLivre(self, bibliotheque, livre):
        dateDuJour = date.today()
        tempsEmprunt = timedelta(days=7)
        dateRetour = dateDuJour + tempsEmprunt
        bibliotheque.livre_liste[bibliotheque.RechercheIndexParLivre(livre)].dispo = False
        bibliotheque.livre_liste[bibliotheque.RechercheIndexParLivre(livre)].retour = dateRetour
        
        self.emprunts.append(livre.ref)
    
    def RendreLivre(self, bibliotheque, livre_ref):
        bibliotheque.livre_liste[bibliotheque.RechercheIndexParRef(livre_ref)].dispo = True
        bibliotheque.livre_liste[bibliotheque.RechercheIndexParRef(livre_ref)].retour = None
        self.compteurLivre += 1
        self.Grade()
        self.emprunts.remove(livre_ref)

    def Grade(self):
        if self.compteurLivre >= 40:
            self.grade = "NAIN"
        elif self.compteurLivre >= 10:
            self.grade = "hobbit"
        elif self.compteurLivre >= 5:
            self.grade = "elf"
        else:
            self.grade = "gollum"

    
    def Clear(self):
        print("\033[H\033[J", end="")
    
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

    def ProlongerEmprunt(self, bibliotheque, livre_ref):
        dateRetour = bibliotheque.livre_liste[bibliotheque.RechercheIndexParRef(livre_ref)].retour 
        dateRetour += timedelta(days=7)
        bibliotheque.livre_liste[bibliotheque.RechercheIndexParRef(livre_ref)].retour = dateRetour
    