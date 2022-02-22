from Livre import Livre

class BD(Livre):
  def __init__(self, titre, auteur, langue, categorie, genre, dispo, couleur, dessinateur,dotation):
    super().__init__(titre, auteur, langue, categorie, genre, dispo, dotation)
    self.couleur = couleur
    self.dessinateur = dessinateur

  def __repr__(self):
    return str(f"Titre : {self.titre}\n" 
      f"Auteur : {self.auteur}\n"
      f"Langue : {self.langue}\n"
      f"Catégories : {self.categorie}\n"
      f"Genre : {self.genre}\n"
      f"Références : {self.ref}\n"
      f"Disponibilité : {self.dispo}\n"
      f"Retour : {self.retour}\n"
      f"Couleur : {self.couleur}\n"
      f"Dessinateur : {self.dessinateur}\n"
      f"dotation : {self.dotation}\n"
    )

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