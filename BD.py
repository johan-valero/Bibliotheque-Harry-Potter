from Livre import Livre

class BD(Livre):
  def __init__(self, titre, auteur, langue, categorie, genre, dispo, couleur, dessinateur,dotation):
    super().__init__(titre, auteur, langue, categorie, genre, dispo, dotation)
    self.couleur = couleur
    self.dessinateur = dessinateur

  def __repr__(self):
    return str(f"[{self.titre}, {self.auteur}, {self.langue}, {self.categorie}, {self.genre}, {self.ref}, {self.dispo}, {self.retour}, {self.couleur}, {self.dessinateur}, {self.dotation}]")

  def AfficherInfo(self):
    print(f"{self.titre}: par {self.auteur} "
      f"Langue : {self.langue}"
      f"Catégories : {self.categorie}"
      f"Genre : {self.genre}"
      f"Références : {self.ref}"
      f"Disponibilité : {self.dispo}"
      f"Retour : {self.retour}"
      f"Couleur : {self.couleur}"
      f"Dessinateur : {self.dessinateur}"
      f"Dotation : {self.dotation}"
    )