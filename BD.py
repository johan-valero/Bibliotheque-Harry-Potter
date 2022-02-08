from Livre import Livre

class BD(Livre):
  def __init__(self, titre, auteur, langue, genre, categorie, ref, dispo, couleur, dessinateur):
    super().__init__(titre, auteur, langue, genre, categorie, ref, dispo)
    self.couleur = couleur
    self.dessinateur = dessinateur

  def __repr__(self):
    return str(f"[{self.titre}, {self.auteur}, {self.categorie}, {self.ref}, {self.dispo}, {self.retour}, {self.couleur}, {self.dessinateur}]")
