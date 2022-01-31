from Personne import *


class User(Personne):

    def __init__(self, Id,  nom, prenom, mdp, emprunts, grade):
        super().__init__(Id,  nom, prenom, mdp)
        self.emprunts = emprunts
        self.grade = grade
