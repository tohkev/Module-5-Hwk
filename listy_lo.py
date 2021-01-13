if __name__ == '__main__':

    food = ['rice', 'beans']
    food.append('broccoli')
    print(food)

    food.extend(['bread', 'pizza'])
    print(food)

    print(food[:2])
    print(food[-1])

    breakfast_string = "eggs,fruit,orange juice"
    breakfast = breakfast_string.split(',')
    print(breakfast)

    breakfast_length = len(breakfast)
    print(breakfast_length)

    give_a_float = 0
    list_of_floats = []
    while give_a_float != 'stop':
        give_a_float = input(
            'Please enter a floating point number (type "stop" to stop): ')
        list_of_floats.append(give_a_float)
        if give_a_float == 'stop':
            list_of_floats.pop()
            for i in range(len(list_of_floats)):
                list_of_floats[i] = float(list_of_floats[i])

    print(f'Your floats are: {list_of_floats}')
    print('Here are some stats: ')
    print(f'Average: {sum(list_of_floats)/len(list_of_floats)}')
    print(f'Smallest Number: {min(list_of_floats)}')
    print(f'Largest Number: {max(list_of_floats)}')
