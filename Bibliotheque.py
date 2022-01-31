class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom 
        self.rayons = []
        self.auteurs = []
        self.livres = []
        self.liste_user = []
  
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

#Ajout User---------------------------------------------------------------------

    def InscriptionUser(self, user):
        self.liste_user.append(user)
        
    def CreerFichierUser(self):
        if not ("Userinscrits.txt"):
            with open("Userinscrits.txt", 'w') as f:
                for user in self.liste_user:
                    f.writelines(user)

    def ExporterUser(self):
        with open("Userinscrits.txt", 'w') as f:
            f.writelines("\n".join(self.liste_user))
            f.close()

    def ImporterUser(self):
        with open("Userinscrits.txt", 'r') as f:
            for i in self.liste_user:
                self.user.append(i)

    def __repr__(self):
        for i in self.liste_user:
            return i

#Ajout Livre---------------------------------------------------------------------

    def InscriptionLivre(self, book):
        self.livres.append(book)
        
    def CreerFichierLivre(self):
        with open("Livresinscrits.txt", 'w') as f:
            for book in self.self.livres:
               f.writelines(book)

    def ExporterLivre(self):
        with open("Livresinscrits.txt", 'w') as f:
            f.writelines("\n".join(self.self.livres))
            f.close()

    def ImporterLivre(self):
        with open("Livresinscrits.txt", 'r') as f:
            for i in self.self.livres:
                self.livres.append(i)

    def AfficherLivre(self):
        for i in self.livres:
            return i


# use = Bibliotheque("bro")
# use.InscriptionUser("broa")
# use.CreerFichierUser()
# print(use)