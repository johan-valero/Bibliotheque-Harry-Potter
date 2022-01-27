class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom 
        self.rayons = []
        self.auteur = []
        self.livres = []
        self.utilisateurs = []

    def InscriptionUser(self, user):
        self.utilisateurs.append(user)
    
    def AfficherDispo(self, livre):
        if livre.dispo == True:
            return livre
        else: 
            print("Le livre choisie n'est pas disponible")
            
    def Rechercher(self, ref):
        for livre in self.rayons:
            if ref.livre == livre:
                return livre  
        return None