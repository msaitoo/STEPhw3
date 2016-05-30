dictionary = open('/usr/share/dict/words', 'r')
word = dictionary.readlines()

'''
Generates the longest word from letters given.
'''
print ("Give letters separated by comma")
letter = raw_input()

ans = []
for w in word:
    w = w.rstrip("\n")                  #takes \n out
    sample = []
    let = letter.split(',')             #string to list
    for i in range(len(w)):
        for x in range(len(let)):
            if w[0] == let[x].upper:    #takes in account for capitalised words
                sample.append(1)
                let.remove(let[x])
                break
            elif w[i] == let[x]:        #lower case words
                sample.append(1)
                let.remove(let[x])
                break
        if len(w) == len(sample):       #checks if the word is made up of let
            ans.append(w)

#Problem: QUITE SLOW :(

answer = max(ans, key=len)              #finds the longest word
print ('''
The longest word generated is [{}] with number of letters {}.
'''.format(answer, len(answer)))