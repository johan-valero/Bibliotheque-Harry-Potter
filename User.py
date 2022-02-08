import datetime
from Personne import Personne
from Livre import *
from Bibliotheque import *
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
            print(j, "-", i.titre, "à rendre avant le", bibliotheque.livre_liste[bibliotheque.RechercheIndex(i)].retour)

    def EmprunterLivre(self, bibliotheque, livre):
        dateDuJour = date.today()
        tempsEmprunt = timedelta(days=7)
        dateRetour = dateDuJour + tempsEmprunt
        bibliotheque.livre_liste[bibliotheque.RechercheIndex(livre)].dispo = False
        bibliotheque.livre_liste[bibliotheque.RechercheIndex(livre)].retour = dateRetour
        

        self.emprunts.append(livre)
    
    def RendreLivre(self, bibliotheque, livre):
        bibliotheque.livre_liste[bibliotheque.RechercheIndex(livre)].dispo = True
        bibliotheque.livre_liste[bibliotheque.RechercheIndex(livre)].retour = None
        self.compteurLivre += 1
        self.Grade()
        self.emprunts.remove(livre)

    def Grade(self):
        if self.compteurLivre >= 40:
            self.grade = "NAIN"
        elif self.compteurLivre >= 10:
            self.grade = "hobbit"
        elif self.compteurLivre >= 5:
            self.grade = "elf"
        else:
            self.grade = "gollum"

    def ChangerMdp(self, new_mdp):
        self.mdp = new_mdp

    def Prolongation(self, bibliotheque, livre):
        durée = input("Désirez-vous prolonger la durée d'emprunt du livre ? : (y/n) \n\t ")
        if durée == "y":
            dateRetour =+ timedelta(days=7)
            bibliotheque.livre_liste[bibliotheque.RechercheIndex(livre)].retour = dateRetour
        else:
            pass
