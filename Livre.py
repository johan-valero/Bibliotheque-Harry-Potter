from datetime import date
import random

class Livre():
  def __init__(self, titre, auteur, langue, categorie, genre, dispo):
    self.titre = titre
    self.auteur = auteur
    self.langue = langue
    self.categorie = categorie
    self.genre = genre
    self.ref = self.RefLivre()
    self.dispo = dispo
    self.retour = None

  def AfficherInfo(self):
    print(f"{self.titre}: par {self.auteur} "
      f"Langue : {self.langue}"
      f"Catégories : {self.categorie}"
      f"Genre : {self.genre}"
      f"Références : {self.ref}"
      f"Disponibilité : {self.dispo}"
      f"Retour : {self.retour}"
    )

  def RefLivre(self):     
    titre = self.titre.upper()
    auteur = self.auteur.upper()
    nombre = random.randint(100000, 999999)
    ref = titre[0] + auteur[0] + str(nombre)
    return ref

  def __repr__(self):
    return str(f"[{self.titre}, {self.auteur}, {self.langue}, {self.categorie}, {self.genre}, {self.ref}, {self.dispo}, {self.retour}]")