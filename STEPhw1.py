
dictionary = open('/usr/share/dict/words', 'r')
word = dictionary.readlines()

'''
Generates the longest word from 16 characters given.
'''
print ("Give 16 characters, NOT separated by space/comma/etc.")
charac = raw_input()

ans = []
testset = set(charac)

for w in word:
    #some code here
            ans.append(w)

#print max(ans, key=len)