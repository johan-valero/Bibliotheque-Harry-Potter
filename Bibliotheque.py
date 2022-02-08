from asyncore import read
from itertools import chain
from os import putenv
from posixpath import split
from User import User
from Livre import Livre
from datetime import date, timedelta

class Bibliotheque:
  def __init__(self, nom):
    self.nom = nom
    self.rayon_liste = []
    self.auteur_liste = []
    self.livre_liste = []
    self.user_liste = []

  def __repr__(self):
    return str(f"[{self.nom}, Catégories : {len(self.rayon_liste)},Livres : {len(self.livre_liste)}, Utilisateurs : {len(self.user_liste)} ]")

# ##################################
#          Import / Export         #
# ##################################
  def RechercherUser(self, id):
    user_trouve = None

    for user in self.user_liste:
      if user.id == id:
        user_trouve = user
    
    return user_trouve
  
  # ########## Import ###########

  def ImporterLivre(self):
    file = open("database/livres.txt", mode='r', encoding="utf-8")
    for line in file.readlines():
      split_line = line.split(';')

      titre = split_line[0]
      auteur = split_line[1]
      langue = split_line[2]
      categorie = split_line[3]
      genre = split_line[4]
      ref = split_line[5]
      dispo = split_line[6]
      retour = split_line[7]

      livre = Livre(titre,auteur,langue,genre,categorie,dispo)

      livre.ref = ref
      livre.retour = retour

      if auteur not in self.auteur_liste:
        self.auteur_liste.append(auteur)

      if categorie not in self.rayon_liste:
        self.rayon_liste.append(categorie)

      self.livre_liste.append(livre)

  def ImporterUser(self):
    users_file = open("database/utilisateurs.txt", mode='r', encoding="utf-8")
    for line in users_file.readlines():
      split_line = line.split(';')

      id_user = split_line[0]
      nom = split_line[1]
      prenom = split_line[2]
      mdp = split_line[3]
      grade = split_line[4]
      emprunts = split_line[5]

      user = User(nom, prenom, mdp)
      user.emprunts = emprunts
      user.grade = grade

      self.user_liste.append(user)

  ############### Export ####################

  def ExporterLivre(self):    
    with open("database/livres.txt", mode='w', encoding="utf-8") as f:
      for i in self.livre_liste:
        chaine = i.titre + ";" + i.auteur + ";" + i.langue + ";" + i.genre + ";" + i.categorie + ";" + i.ref + ";" + str(i.dispo) + ";" + str(i.retour) + "\n"
        f.write(chaine)

  def ExporterUser(self):
    with open("database/utilisateurs.txt", mode='w', encoding="utf-8") as f:
      for i in self.user_liste:
        chaine = i.id + ";" + i.nom + ";" + i.prenom + ";" + i.mdp + ";" + str(i.emprunts) + ";" + i.grade + "\n"
        f.write(chaine)

  # ############################ #
  #         Rechercher           #
  # ############################ #
  def RechercherLivreParRef(self, ref):
    livre_trouve = None

    for livre in self.livre_liste:
      if livre.ref == ref:
        livre_trouve = livre

    return livre_trouve

  def RechercherLivreParTitre(self, titre):
    livres_trouves = []

    for livre in self.livre_liste:
      if livre.titre == titre:
        livres_trouves.append(livre)

    if len(livres_trouves) == 0:
      print("Aucun livre trouvé")

    return livres_trouves

  def RechercherLivreParCategorie(self, categorie):
    livres_trouves = []

    if categorie not in self.rayon_liste:
      print("Aucun livre trouvé")

    else:
      for livre in self.livre_liste:
        if livre.categorie == categorie:
          livres_trouves.append(livre)

      if len(livres_trouves) == 0:
        print("Aucun livre trouvé")

    return livres_trouves

  def RechercherLivreParAuteur(self, auteur):
    livres_trouves = []

    if auteur not in self.auteur_liste:
      print("Aucun livre trouvé")

    else:
      for livre in self.livre_liste:
        if livre.auteur == auteur:
          livres_trouves.append(livre)

      if len(livres_trouves) == 0:
        print("Aucun livre trouvé")

    return livres_trouves

  def RechercherLivreParGenre(self, genre):
    livres_trouves = []
    
    for livre in self.livre_liste:
      if livre.genre == genre:
        livres_trouves.append(livre)

    if len(livres_trouves) == 0:
      print("Aucun livre trouvé")

    return livres_trouves

  def RechercherLivreParLangue(self, langue):
    livres_trouves = []

    for livre in self.livre_liste:
      print("langue", livre.langue)
      if livre.langue == langue:
        livres_trouves.append(livre)

    if len(livres_trouves) == 0:
      print("Aucun livre trouvé")

    return livres_trouves

  #################################################
  
  def AfficherDispo(self):
    livresDispos = []

    for livre in self.livre_liste:
      if livre.dispo:
        livresDispos.append(livre)
    
    print('Livres disponibles :')
    for i in livresDispos:
      print(i)

  def RechercheIndex(self, livre):
    j = 0
    for l in self.livre_liste:
      j += 1
      if l.ref == livre.ref:
        return j - 1
