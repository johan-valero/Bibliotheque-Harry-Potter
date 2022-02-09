from msilib import Table
from User import *
from Livre import *
from BD import *
from datetime import date, timedelta
import ast

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
		with open("database/livres.txt", mode='r', encoding="utf-8") as file:
			for line in file.readlines():
				split_line = line.split(';')
				if len(split_line) >= 8: 
					titre = split_line[0]
					auteur = split_line[1]
					langue = split_line[2]
					categorie = split_line[3]
					genre = split_line[4]
					ref = split_line[5]
					dispo = split_line[6]
					retour = split_line[7]

					if dispo == "True":
						dispo = True
					elif dispo == "False":
						dispo = False

					if retour == "None":
						retour = None

					if len(split_line) == 10:
						couleur = split_line[8]
						dessinateur = split_line[9]

						if couleur == "True":
							couleur = True
						elif couleur == "False":
							couleur = False

						bidule = BD(titre,auteur,langue,categorie,genre,dispo, couleur, dessinateur)

						bidule.ref = ref
						bidule.retour = retour
					
					else:
						bidule = Livre(titre,auteur,langue,categorie,genre,dispo)

						bidule.ref = ref
						bidule.retour = retour

					if auteur not in self.auteur_liste:
						self.auteur_liste.append(auteur)

					if categorie not in self.rayon_liste:
						self.rayon_liste.append(categorie)

					self.livre_liste.append(bidule)
			file.close()

	def ImporterUser(self):
		with open("database/utilisateurs.txt", mode='r', encoding="utf-8") as users_file:
			for line in users_file.readlines():
				split_line = line.split(';')
				input(split_line)

				if len(split_line) == 8:            
					id_user = split_line[0]
					nom = split_line[1]
					prenom = split_line[2]
					mdp = split_line[3]
					emprunts = split_line[4]
					grade = split_line[5]
					compteur_livre = split_line[6]
					maison = split_line[7]

					user = User(nom, prenom, mdp)
					user.emprunts = ast.literal_eval(emprunts)
					user.grade = grade
					user.id = id_user
					user.compteur_livre = int(compteur_livre)
					if maison == "None":
						maison = None
					user.maison = maison

					self.user_liste.append(user)
			users_file.close()

	############### Export ####################

	def ExporterLivre(self):    
		with open("database/livres.txt", mode='w', encoding="utf-8") as f:
			for i in self.livre_liste:
				if isinstance(i, BD):
					chaine = i.titre + ";" + i.auteur + ";" + i.langue + ";" + i.categorie + ";" + i.genre + ";" + i.ref + ";" + str(i.dispo) + ";" + str(i.retour) + ";" + str(i.couleur) + ";" + i.dessinateur
					f.write(chaine)

				elif isinstance(i, Livre):
					chaine = i.titre + ";" + i.auteur + ";" + i.langue + ";" + i.categorie + ";" + i.genre + ";" + i.ref + ";" + str(i.dispo) + ";" + str(i.retour)
					f.write(chaine)
			f.close()

	def ExporterUser(self):
		with open("database/utilisateurs.txt", mode='w', encoding="utf-8") as f:
			for i in self.user_liste:
				chaine = i.id + ";" + i.nom + ";" + i.prenom + ";" + i.mdp + ";" + str(i.emprunts) + ";" + i.grade + ";" + str(i.compteur_livre) + ";" + str(i.maison)
				f.write(chaine)
			f.close()
			
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

	def RechercheIndexParLivre(self, livre):
		j = 0
		for l in self.livre_liste:
			j += 1
			if l.ref == livre.ref:
				return j - 1
	
	def RechercheIndexParRef(self, livre_ref):
		j = 0
		for l in self.livre_liste:
			j += 1
			if l.ref == livre_ref:
				return j - 1


	