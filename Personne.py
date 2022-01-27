class Personne:
    def __init__(self, nom, prenom, mdp):
        self.nom = nom
        self.prenom = prenom
        self.mdp = mdp
        
    def __repr__(self):
        return self.nom