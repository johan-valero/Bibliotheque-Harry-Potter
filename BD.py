from Livre import Livre

class BD(Livre):
  def __init__(self, titre, auteur, langue, categorie, genre, ref, dispo, couleur, dessinateur):
    super().__init__(titre, auteur, langue, categorie, genre, ref, dispo)
    self.couleur = couleur
    self.dessinateur = dessinateur

  def __repr__(self):
    return str(f"[{self.titre}, {self.auteur}, {self.langue}, {self.categorie}, {self.genre}, {self.ref}, {self.dispo}, {self.retour}, {self.couleur}, {self.dessinateur}]")
