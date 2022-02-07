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

  def ImporterLivre(self):
    file = open("database/livres.txt", mode='r', encoding="utf-8")
    for line in file.readlines():
      splitLine = line.split(' ; ')

      titre = splitLine[0]
      auteur = splitLine[1]
      langue = splitLine[2]
      categorie = splitLine[3]
      genre = splitLine[4]
      ref = splitLine[5]
      dispo = splitLine[6]
      retour = splitLine[7]

      livre = Livre(titre,auteur,langue,genre,categorie,dispo)

      livre.ref = ref
      livre.retour = retour

      if auteur not in self.auteur_liste:
        self.auteur_liste.append(auteur)

      if categorie not in self.rayon_liste:
        self.rayon_liste.append(categorie)

      self.livre_liste.append(livre)

  def ImporterUser(self):
    usersFile = open("database/utilisateurs.txt", mode='r', encoding="utf-8")
    empruntsFile = open("database/emprunts.txt", mode='r', encoding="utf-8")

    for line in usersFile.readlines():
      splitLine = line.split(' ; ')

      nom = splitLine[0]
      prenom = splitLine[1]
      mdp = splitLine[2]
      grade = splitLine[3]
      emprunts = []

      user = User(nom, prenom, mdp, emprunts, grade)

      self.user_liste.append(user)
    
    for line in empruntsFile.readlines():
      lineSplit = line.strip().split(" ; ")
      idUser = lineSplit[0]
      refLivre = lineSplit[1]

      user = self.rechercherUser(idUser)
      livre = self.rechercherLivreParRef(refLivre)

      if user and livre:
        user.emprunts.append(livre)

  def RechercherUser(self, id):
    userTrouve = None

    for user in self.user_liste:
      if user.id == id:
        userTrouve = user
    
    return userTrouve

  def RechercherLivreParRef(self, ref):
    livreTrouve = None

    for livre in self.livre_liste:
      if livre.ref == ref:
        livreTrouve = livre

    return livreTrouve

  def RechercherLivreParTitre(self, titre, dispo):
    livresTrouves = []

    for livre in self.livre_liste:
      if livre.titre == titre:
        livresTrouves.append(livre)

    if len(livresTrouves) == 0:
      print("Aucun livre trouvé")

    return livresTrouves

  def RechercherLivreParCategorie(self, categorie):
    livresTrouves = []

    if categorie not in self.rayon_liste:
      print("Aucun livre trouvé")
      return None

    for livre in self.livre_liste:
      if livre.categorie == categorie:
        livresTrouves.append(livre)

    if len(livresTrouves) == 0:
      print("Aucun livre trouvé")

    return livresTrouves

  def RechercherLivreParAuteur(self, auteur):
    livresTrouves = []

    if auteur not in self.auteur_liste:
      print("Aucun livre trouvé")
      return None

    for livre in self.livre_liste:
      if livre.auteur == auteur:
        livresTrouves.append(livre)

    if len(livresTrouves) == 0:
      print("Aucun livre trouvé")

    return livresTrouves

  def RechercherLivreParGenre(self, genre):
    livresTrouves = []

    for livre in self.livre_liste:
      if livre.genre == genre:
        livresTrouves.append(livre)

    if len(livresTrouves) == 0:
      print("Aucun livre trouvé")

    return livresTrouves

  def RechercherLivreParLangue(self, langue):
    livresTrouves = []

    for livre in self.livre_liste:
      print("langue", livre.langue)
      if livre.langue == langue:
        livresTrouves.append(livre)

    if len(livresTrouves) == 0:
      print("Aucun livre trouvé")

    return livresTrouves

  def AfficherDispo(self, livres):
    livresDispos = []

    for livre in livres:
      if livre.dispo:
        livresDispos.append(livre)
    
    print('Livres disponibles :', livresDispos)

  def EmprunterLivre(self, user, livre):
    dateDuJour = date.today()
    tempsEmprunt = timedelta(days=7)
    dateRetour = dateDuJour + tempsEmprunt

    livre.dispo = False
    livre.retour = dateRetour

    user.emprunts.append(livre)
  
  def RendreLivre(self, user, livre):
    livre.dispo = True
    livre.retour = None
    indexLivre = user.emprunts.index(livre)

    del user.emprunts[indexLivre]

  def __repr__(self):
    return str(f"[{self.nom}, Catégories : {len(self.rayon_liste)},Livres : {len(self.livre_liste)}, Utilisateurs : {len(self.user_liste)} ]")
    