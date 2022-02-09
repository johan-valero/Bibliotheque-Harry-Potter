class Personne:
    def __init__(self, nom, prenom, mdp):
        self.nom = nom
        self.prenom = prenom
        self.mdp = mdp
        self.id = self.IdUser()
    
    def IdUser(self):
        Id = str(self.nom[0] + "." + self.prenom)
        return Id