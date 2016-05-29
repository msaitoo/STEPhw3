
dictionary = open('/usr/share/dict/words', 'r')
word = dictionary.readlines()

'''
Generates the longest word from 16 characters given.
'''
print ("Give 16 characters, NOT separated by space/comma/etc.")
charac = raw_input()

poss1 = []
for i in range(len(word)):
    if (len(word[i])-1) <= 16:
        poss1.append(word[i])
poss2 = []
poss3 = []
for x in range(16):
    for i in range(len(poss1)):
        if charac[x] == poss1[i][0]:
            poss2.append(poss1[i])
for y in range(len(poss2)):
        if charac[0] == poss2[y][len(poss2[y])-2]:
            poss3.append(poss2[y])