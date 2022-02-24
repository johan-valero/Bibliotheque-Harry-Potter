                                                    # ============== TODO LIST ==============


# Admin
# TODO 01: Créer Classe
# TODO 02: Ajout Méthodes
# TODO 03: Accès au menu admin
# TODO 04: La méthode référence de livre pas encore utilisé 

# Recherche ========================================================================================================

# TODO 05: Revoir affichage (Ajouter filtres )
# TODO 06: Cacher l’affichage par référence pour les Users 
# TODO 07: Revoir affichage et recherche livre
# ///TODO 08: Problème de retour 1 pour RecherchParRef et liste pour les autres
# TODO 09: Cacher affichage et recherche par réf du user (accès que pour l’admin)

# Gestion Globale ========================================================================================================

# TODO 10: Ajouter Gitignore
# TODO 11: Revoir import des fichiers pour enlever redondance fonction clear et check# TODO 2:in

# Générale ========================================================================================================


# display
# TODO 12: Transfert des ASCII sur les fonctions
# TODO 13: Améliorer affichage du château au début du main (ajout couleur, revoir trait en-dessous, l'enjoliver) 
# TODO 14: Revoir affichage résultat recherche 

# Corrections 
    # Erreurs
    # TODO 15: Modifier Catégorie et genre
    # ///TODO 16: Changer le nom de bibliothèque (Poney_fringant ne fais pas partie de Harry Wesh)
    # ///TODO 17: Suppression de f.close (sur les with open)
    # TODO 18: Correction de l’attribut .retour de livre et BD (qui n’est pas Date Time) sur l'import / Export
    # TODO 19: Corriger ProlongerEmprunt l'input prend 0

    # Logique
    # TODO 20: La prolongation d’un emprunt est limité uniquement à 7 jours et se fait sans limitation (On peut prolonger à volonté).

# Optimisation 
    # main
    # TODO 21: Ajouter fonction start / quitter pour vider le main 
    # TODO 22: Transfert menu 2 : 2 # TODO 1: Emprunter dans classes la classe User pour réduire le main
    # TODO 23: Mettre inscription User dans le User

    # Classes
    # TODO 24: Mettre les points des maisons dans un dico 
    # TODO 25: Revoir REPR et les unifier (nom de l’attribut: Valeur de l’attribut )
    # TODO 26: Rajout de Str pour remplacer afficher 
    # TODO 27: Utilisation des str des classes pour affichage (simple)
    # TODO 28: Ajout de getter, setter dans les classes (très lourd à mettre en place)
    # TODO 29: Les recherches de livres ne donnent pas droit à l’erreur (Pas de faute ou d’oublies de majuscules). 

# Ergonomie
# TODO 30: Rechercher par Titre doit être revu en ajoutant code couleur pour distinguer dispo ou non 
# TODO 31: Connexion direct après création de compte 
# TODO 32: Afficher les livres lors des emprunts (dispo en vert , non dispo en rouge)
# TODO 33: L’utilisateur ne peut pas voir son nombre de points ou son grade. 
# TODO 34: Le nom de l’utilisateur n’est pas affiché lorsqu'il est connecté. 

# Aide à la lecture du code
# TODO 35: Ajout de commentaire pour plus de clarté 
# TODO 36: Supprimer commentaire inutile
# TODO 37: Normalisation et optimisation du code 
# TODO 38: Ordonner les méthodes 

# Amélioration Sécurité
# TODO 39: Ajouter déconnexion si changement de mot de passe 3 fois d’affiler
# TODO 40: Compteur tentative sur rechecking mot de passe
# TODO 41: Problème de sécurité sur l'authentification (un hackeur connaît l’existence d’un pseudo)
# TODO 42: Ajouter double check sur mot pour la création de compte
# TODO 43: Cacher le mot de passe à la saisie 
# TODO 44: Problème de sur le strict des recherches (Regex, Str in ,chaîne de caractère, utilisation du    Lowercase())

# Features
# TODO 45: Changer ordre attribut (Pour les réservation)pour classes Livres et BD pour précision future  avec admin : enregistrer livres étant pas disponible.
# TODO 46: Ajouter les réservations  

# Ajouter Classes pour mise en place Médiathèque (pas trop top dans un monde de magie au pire leur emprunt induit un malus xD)
# TODO 47: Classe CD
# TODO 48: Classe DVD
