from classes.Bibliotheque import Bibliotheque

# TODO : Enregistrer nouveau utilisateur
# TODO : Connecter utilisateur
# TODO : Changer mdp utilisateur
# xTODO : Afficher les livres disponibles par catégories/auteur/genre/langue
# xTODO : Recherche un livre, une catégorie, un auteur, un genre
# xTODO : Emprunter/rendre livre
# TODO : Prolonger un emprunt
# TODO: Exporter livres dans 'database' lors sortie programme
# TODO: Exporter users (et emprunts) dans 'database' lors sortie programme

biblio = Bibliotheque("BU Toulouse")

biblio.importerLivres()
biblio.importerUsers()

livre = biblio.livres[2]
user = biblio.liste_users[0]

biblio.preter(user, livre)
biblio.recuperer(user, user.emprunts[1])