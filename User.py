from Personne import Personne
from Livre import *
from Bibliotheque import *
from datatime import date, timedelta

class User(Personne):
  def __init__(self, nom, prenom, mdp, emprunts, grade):
    super().__init__(nom, prenom, mdp)
    self.emprunts = emprunts
    self.grade = grade
  
  def __repr__(self):
    return str(f"[{self.nom}, {self.prenom}, {self.mdp}, {self.emprunts}, {self.grade}]")

  def AfficherEmprunts(self):
    print(self.emprunts)

  def EmprunterLivre(self, user, livre):
    dateDuJour = date.today()
    tempsEmprunt = timedelta(days=7)
    dateRetour = dateDuJour + tempsEmprunt

    livre.dispo = False
    livre.retour = dateRetour

    user.emprunts.append(livre)
  
  def RendreLivre(self, user, livre):
    livre.dispo = True
    livre.retour = None
    indexLivre = user.emprunts.index(livre)

    del user.emprunts[indexLivre]

# def Grade (self):
#     grades = {"moldu":[0,1],"sangdebourge":[2,5],"sorcier":[6,10],"auror":[11,40]}

# emprunts = 0

