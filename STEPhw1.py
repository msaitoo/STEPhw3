dictionary = open('/usr/share/dict/words', 'r')
word = dictionary.readlines()

'''
Generates the longest word from 16 letters given.
'''
print ("Give 16 letters separated by comma")
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
    
#need to solve:
        #1. exclude the ones with non-given letters: CHECK
        #2. consider duplicate letters: CHECK
        #3. capitalised words... :(
        #4. VERY INEFICCIENT orz

print max(ans, key=len)