class Personne:
    def __init__(self, nom, prenom, mdp):
        self.id = nom[0] + "." + prenom[0]
        self.nom = nom
        self.prenom = prenom
        self.mdp = mdp
    
    def IdUser(nom, prenom):
        Id = str(nom[0]+"."+prenom)
        return Id