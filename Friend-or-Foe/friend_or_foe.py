def friend(x):
    friends = []
    for el in x:
        if len(el) == 4:
            friends.append(el)
    return friends


print(friend(["Ryan", "Kieran", "Jason", "Yous"]))
