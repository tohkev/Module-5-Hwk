if __name__ == '__main__':
    pokedex = {
        'Venosaur': ['Grass', 'Poison'],
        'Charizard': ['Fire', 'Flying'],
        'Blastoise': ['Water']
    }
    del pokedex['Blastoise']
    print(pokedex.keys())
