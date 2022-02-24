import random

# TODO: Mettre attribut dispo à la fin pour le rendre optionnel (dispo=True)
# ! Attention : Grosse modifs en perspective notament sur :
# ! toute création de livre
# ! dans l'import et l'export

class Livre():
  def __init__(self, titre, auteur, langue, genre, categorie, dispo, dotation):
    self.titre = titre
    self.auteur = auteur
    self.langue = langue
    self.genre = genre
    self.categorie = categorie
    self.ref = self.RefLivre()
    self.dispo = dispo
    self.retour = None
    self.dotation = dotation

  def AfficherInfo(self):
    print(f"{self.titre}: par {self.auteur} "
      f"Langue : {self.langue}"
      f"Genre : {self.genre}"
      f"Catégories : {self.categorie}"
      f"Références : {self.ref}"
      f"Disponibilité : {self.dispo}"
      f"Retour : {self.retour}"
      f"Dotation : {self.dotation}"
    )

  def RefLivre(self):     
    titre = self.titre.upper()
    auteur = self.auteur.upper()
    nombre = random.randint(100000, 999999)
    ref = titre[0] + auteur[0] + str(nombre)
    return ref

  def __repr__(self):
    return str(f"Titre : {self.titre}\n" 
      f"Auteur : {self.auteur}\n"
      f"Langue : {self.langue}\n"
      f"Genre : {self.genre}\n"
      f"Catégories : {self.categorie}\n"
      f"Références : {self.ref}\n"
      f"Disponibilité : {self.dispo}\n"
      f"Retour : {self.retour}\n"
      f"Dotation : {self.dotation}\n"
    )