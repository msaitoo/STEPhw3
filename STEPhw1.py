dictionary = open('/usr/share/dict/words', 'r')
word = dictionary.readlines()

'''
Generates the longest word from letters given.
'''
print ("Give letters separated by comma")
letter = raw_input()

ans = []
for w in word:
    w = w.rstrip("\n")
    sample = []
    let = letter.split(',')
    for i in range(len(w)):
        for x in range(len(let)):
                if w[i] == let[x]:
                    sample.append(w)
                    let.remove(let[x])
                    break
        if len(w) == len(sample):
            ans.append(w)
    
#Problems:
    #1. ignores capitalised words when only small letters given
    #2. VERY SLOW :(

print max(ans, key=len)