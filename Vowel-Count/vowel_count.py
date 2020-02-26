def getCount(inputStr):
    num_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for el in vowels:
        num_vowels += inputStr.count(el)
    return num_vowels


print(getCount("abracadabra"))
print(getCount("aoooeuiuoiiuaaaaaa"))
