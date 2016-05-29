
dictionary = open('/usr/share/dict/words', 'r')
word = dictionary.readlines()

'''
Generates the longest word from 16 letters given.
'''
print ("Give 16 letters without space/comma/etc between them")
let = raw_input()

ans = []

for w in word:
    if all(i in w for i in let):
        #need to solve:
        #1. exclude the ones with non-given letters
        #2. consider duplicate letters
        #3. don't have to use all the letters given
        ans.append(w)

#print max(ans, key=len)