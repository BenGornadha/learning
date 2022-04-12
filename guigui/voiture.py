class voiture:

    def __init__(self, modele, marque, bite):
        self.modele = modele
        self.marque = marque
        self.bite = bite

    def is_for_rich(self):
        if self.marque == "ferrari":
            return True
        else :
            return False

