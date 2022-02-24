from User import *

class Admin(User):
    def __init__(self, id, mdp):
        super().__init__(id, mdp)
        self.id = "Voldemort"

    def AfficherLivre(self):
        print()
    
    def AjouterLivre(self):
        print()

    def ModifierLivre(self):
        print()

    def SupprimerLivre(self):
        print()

    def AvadaKedavraListeLivre(self, bibliotheque):
        print(f"Suppression base de données livres de {bibliotheque.nom}")
        safe = input("Confirmez suppression avec 'y'\n> ")
        save = print("Voulez-vous faire une sauvegarde ?")
        input("'y' / 'n'")


    def AvadaKedavraListeUser(self, bibliotheque):
        print("Suppression liste utilisateurs")

    def AvadaKedavraClassement(self, bibliotheque):
        print("Suppression données classement des quatres Maisons")

    def AfficherUser(self):
        print()

    def AjouterUser(self):
        print()

    def ModifierUser(self):
        print()

    def SupprimerUser(self):
        print()
    
    def ExporterDonnees(self):
        print()

    def AfficherEmprunt(self):
        print()

    def ExporterEmprunt(self):
        print()
    
    def ProlongerEmprunt(self):
        print()

    def AttribuerEmprunt(self):
        print()

    