from datetime import date
import random

class Livre():

    def __init__(self,titre, auteur, langue,
                 genre, categorie, ref, dispo):
        self.titre = titre
        self.auteur = auteur
        self.langue = langue
        self.genre = genre
        self.categorie = categorie
        self.ref = ref
        self.dispo = dispo
        self.retour = date
 
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
        rand =""
        for n in range (6):
            alea = random.randint(1, 9)
            rand += str(alea)
        Ref = titre[0] + auteur[0] + rand
        return Ref


