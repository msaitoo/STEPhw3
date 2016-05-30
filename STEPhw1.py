dictionary = open('/usr/share/dict/words', 'r')
word = dictionary.readlines()

'''
Generates the longest word from 16 letters given.
'''
print ("Give 16 letters without space/comma/etc between them")
let = raw_input()

ans = []
for w in word:
    w = w.rstrip("\n")
    sample = []
    for i in range(len(w)):
        if len(w) <= len(let) and any(w[i] == x for x in let):
            sample.append(w)
        if (len(sample) == len(w)):
            ans.append(w)
            
#need to solve:
        #1. exclude the ones with non-given letters: CHECK
        #2. consider duplicate letters
        #3. capitalised words... :(
        #4. efficiency orz

print max(ans, key=len)