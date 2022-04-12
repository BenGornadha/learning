
class Person:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def get_identite_de_la_personne(self):
        return self.nom + " " + self.prenom

if __name__ == '__main__':

    premiere_personne = Person(nom="Bats",prenom="Guillaume")
    deuxieme_personne = Person(nom=1,prenom=[1.2,1.4])

    print(premiere_personne.get_identite_de_la_personne())