from msilib import Table
from User import *
from datetime import date, timedelta
import ast

class Bibliotheque:
	def __init__(self, nom):
		self.nom = nom
		self.rayon_liste = []
		self.auteur_liste = []
		self.livre_liste = []
		self.user_liste = []
		self.gryffondor_pts = 0
		self.poufsouffle_pts = 0
		self.serdaigle_pts = 0
		self.serpentard_pts = 0

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
				
				if len(split_line) == 9: 
					titre = split_line[0]
					auteur = split_line[1]
					langue = split_line[2]
					genre = split_line[3]
					categorie = split_line[4]
					ref = split_line[5]
					dispo = split_line[6]
					retour = split_line[7]
					dotation = split_line[8][:-1]

					if dispo == "True":
						dispo = True
					elif dispo == "False":
						dispo = False

					if retour == "None":
						retour = None

					dotation = int(dotation)
					bidule = Livre(titre,auteur,langue,genre,categorie,dispo,dotation)

					bidule.ref = ref
					bidule.retour = retour

					if auteur not in self.auteur_liste:
						self.auteur_liste.append(auteur)

					if categorie not in self.rayon_liste:
						self.rayon_liste.append(categorie)

					self.livre_liste.append(bidule)
				
				# BD
				elif len(split_line) == 11:
					titre = split_line[0]
					auteur = split_line[1]
					langue = split_line[2]
					genre = split_line[3]
					categorie = split_line[4]
					ref = split_line[5]
					dispo = split_line[6]
					retour = split_line[7]
					dotation = split_line[8]
					couleur = split_line[9]
					dessinateur = split_line[10][:-1]

					if dispo == "True":
						dispo = True
					elif dispo == "False":
						dispo = False

					if retour == "None":
						retour = None

					if couleur == "True":
						couleur = True
					elif couleur == "False":
						couleur = False
					
					dotation = int(dotation)
					bidule = BD(titre,auteur,langue,genre,categorie,dispo, dotation, couleur, dessinateur)

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

				if len(split_line) == 8:            
					id_user = split_line[0]
					nom = split_line[1]
					prenom = split_line[2]
					mdp = split_line[3]
					emprunts = split_line[4]
					grade = split_line[5]
					compteur_livre = split_line[6]
					maison = split_line[7][:-1]

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

	def ImportClassement(self):
		with open("database/classement.txt", mode='r', encoding="utf-8") as classement_file:
			for line in classement_file.readlines():
				split_line = line.split(';')

				pts_gryffondor = split_line[0]
				pts_poufsouffle = split_line[1]
				pts_serdaigle = split_line[2]
				pts_serpentard = split_line[3][:-1]

				self.gryffondor_pts = int(pts_gryffondor)
				self.poufsouffle_pts = int(pts_poufsouffle)
				self.serdaigle_pts = int(pts_serdaigle)
				self.serdaigle_pts = int(pts_serpentard)
			classement_file.close()

	############### Export ####################

	def ExporterLivre(self):    
		with open("database/livres.txt", mode='w', encoding="utf-8") as f:
			for i in self.livre_liste:
				if isinstance(i, BD):
					chaine = i.titre + ";" + i.auteur + ";" + i.langue + ";" + i.genre + ";" + i.categorie + ";" + i.ref + ";" + str(i.dispo) + ";" + str(i.retour) + ";" + str(i.dotation) + ";" + str(i.couleur) + ";" + i.dessinateur 
					f.write(chaine+"\n") 

				elif isinstance(i, Livre):
					chaine = i.titre + ";" + i.auteur + ";" + i.langue + ";" + i.genre + ";" + i.categorie + ";" + i.ref + ";" + str(i.dispo) + ";" + str(i.retour) + ";" + str(i.dotation)
					f.write(chaine+"\n") 
			

	def ExporterUser(self):
		with open("database/utilisateurs.txt", mode='w', encoding="utf-8") as f:
			for i in self.user_liste:
				chaine = i.id + ";" + i.nom + ";" + i.prenom + ";" + i.mdp + ";" + str(i.emprunts) + ";" + i.grade + ";" + str(i.compteur_livre) + ";" + str(i.maison)
				f.write(chaine+"\n")
			

	def ExporterClassement(self):
		with open("database/classement.txt", mode='w', encoding="utf-8") as f:
			chaine = str(self.gryffondor_pts) + ";" + str(self.poufsouffle_pts) + ";" + str(self.serdaigle_pts) + ";" + str(self.serpentard_pts)
			f.write(chaine+"\n")
			

			
	# ############################ #
	#         Rechercher           #
	# ############################ #
	def RechercherLivreParRef(self, ref):
		livre_trouve = None

		for livre in self.livre_liste:
			if livre.ref.lower() == ref.lower():
				livre_trouve = livre

		return livre_trouve

	def RechercherLivreParTitre(self, titre):
		livres_trouves = []

		for livre in self.livre_liste:
			if titre.lower() in livre.titre.lower():
				livres_trouves.append(livre)

		if len(livres_trouves) == 0:
			print("Aucun livre trouvé")

		elif len(livres_trouves) > 0:
				print("Quel livre voulez-vous emprunter ?")

		return livres_trouves	

	def RechercherLivreParCategorie(self, categorie):
		livres_trouves = []

		for livre in self.livre_liste:
			if categorie.lower() in livre.categorie.lower():
				livres_trouves.append(livre)

		if len(livres_trouves) == 0:
			print("Aucun livre trouvé")

		elif len(livres_trouves) > 0:
			print("Quel livre voulez-vous emprunter ?")

		return livres_trouves

	def RechercherLivreParAuteur(self, auteur):
		livres_trouves = []

		for livre in self.livre_liste:
			if auteur.lower() in livre.auteur.lower():
				livres_trouves.append(livre)

		if len(livres_trouves) == 0:
			print("Aucun livre trouvé")
		
		elif len(livres_trouves) > 0:
			print("Quel livre voulez-vous emprunter ?")

		return livres_trouves

	def RechercherLivreParGenre(self, genre):
		livres_trouves = []
		
		for livre in self.livre_liste:
			if genre.lower() in livre.genre.lower():
				livres_trouves.append(livre)

		if len(livres_trouves) == 0:
			print("Aucun livre trouvé")

		elif len(livres_trouves) > 0:
			print("Quel livre voulez-vous emprunter ?")

		return livres_trouves

	def RechercherLivreParLangue(self, langue):
		livres_trouves = []

		
		for livre in self.livre_liste:
			if langue.lower() in livre.langue.lower():
				livres_trouves.append(livre)
		
		if len(livres_trouves) == 0:
			print("Aucun livre trouvé")

		elif len(livres_trouves) > 0:
			print("Quel livre voulez-vous emprunter ?")
	
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

	#################################################			

	def AfficherLivresTotaux(self):
		for b in self.livre_liste:
			print(b)