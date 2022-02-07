from datetime import date
import random

class Livre():
  def __init__(self,titre,auteur,langue,genre,categorie,dispo):
    self.titre = titre
    self.auteur = auteur
    self.langue = langue
    self.genre = genre
    self.categorie = categorie
    self.ref = None
    self.dispo = dispo
    self.retour = None

  def AfficherInfo(self):
    print(f"{self.titre}: par {self.auteur} "
      f"Langue : {self.langue}"
      f"Genre : {self.genre}"
      f"Catégories : {self.categorie}"
      f"Références : {self.ref}"
      f"Disponibilité : {self.dispo}"
      f"Retour : {self.retour}"
    )

  def RefLivre(self):     
    titre = self.titre.upper()
    auteur = self.auteur.upper()
    nombre = random.randint(100000, 999999)
    self.ref = titre[0] + auteur[0] + str(nombre)

  def __repr__(self):
    return str(f"[{self.titre}, {self.auteur}, {self.categorie}, {self.ref}, {self.dispo}]")