from Livre import *

class BD(Livre):
    def __init__(self,titre, auteur, langue,
                 genre, categorie, ref, dispo):
        super().__init__(titre, auteur, langue, genre, categorie, ref, dispo )
