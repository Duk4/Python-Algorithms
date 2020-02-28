def find_needle(haystack):
    i = haystack.index('needle')
    return 'found the needle at position ' + str(i)


print(find_needle(['hay', 'junk', 'needle', 'hay', 'hay',
                   'moreJunk', 'randomJunk']))
