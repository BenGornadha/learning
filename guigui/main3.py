from guigui.voiture import voiture

if __name__ == '__main__':
    une_variable = 1
    premiere_voiture = voiture(marque="renault", modele="kangoo", bite="dure" )
    deuxieme_voiture = voiture(marque= "ferrari", modele="batman", bite="elastic")
    print(premiere_voiture.is_for_rich())
    print(deuxieme_voiture.is_for_rich())





