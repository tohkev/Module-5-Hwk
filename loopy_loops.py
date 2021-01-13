if __name__ == '__main__':
    pokemon = ('pikachu', 'charmander', 'bulbasaur')
    print(pokemon[1])

    starter1 = pokemon[0]
    starter2 = pokemon[1]
    starter3 = pokemon[2]

    print(starter1, starter2, starter3)

    name_tuple = tuple('Kevin')
    print(name_tuple)

    is_there_i = 'i' in name_tuple
    print(is_there_i)

    for i in range(2, 11):
        print(i)

    i = 2
    while i < 11:
        print(i)
        i += 1

    string = 'This is a simple string'
    for letter in string:
        print(letter)

    set_of_strings = ('this', 'is', 'a', 'simple', 'set')
    for i in range(3):
        for word in set_of_strings:
            print(word)
