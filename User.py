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

    def AfficherEmprunts(self):
        print(self.emprunts)

    def EmprunterLivre(self, bibliotheque, livre):
        dateDuJour = date.today()
        tempsEmprunt = timedelta(days=7)
        dateRetour = dateDuJour + tempsEmprunt
        bibliotheque.livre_liste[livre.RechercheIndex()].dispo = False
        bibliotheque.livre_liste[livre.RechercheIndex()].retour = dateRetour

        self.emprunts.append(livre)
    
    def RendreLivre(self, bibliotheque, livre):
        bibliotheque.livre_liste[livre.RechercheIndex()].dispo = True
        bibliotheque.livre_liste[livre.RechercheIndex()].retour = None
        self.compteurLivre += 1
        self.Grade()
        self.emprunts.remove(livre)

    def Grade(self):
        if self.emprunts >= 40:
            self.grade = "NAIN"
        elif self.emprunts >= 10:
            self.grade = "hobbit"
        elif self.emprunts >= 5:
            self.grade = "elf"
        else:
            self.grade = "gollum"
