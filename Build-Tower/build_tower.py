def tower_builder(n):
    num_spaces = n-1
    stars = 1
    tower = []
    while num_spaces > -1:
        spaces = ' ' * num_spaces
        string = spaces + (stars * '*') + spaces
        tower.append(string)
        num_spaces -= 1
        stars += 2
    return tower


print(tower_builder(3))
