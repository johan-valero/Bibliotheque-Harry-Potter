from classes.Personne import Personne

class User(Personne):
  def __init__(self, nom, prenom, mdp, emprunts, grade):
    super().__init__(nom, prenom, mdp)
    self.emprunts = emprunts
    self.grade = grade
  
  def __repr__(self):
    return str(f"[{self.nom}, {self.prenom}, {self.mdp}, {self.emprunts}, {self.grade}]")

  def AfficherEmprunts(self):
    print(self.emprunts)
