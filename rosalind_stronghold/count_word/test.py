
word = {}
f = open('rosalind_ini6.txt','r')
d = f.readline().split()
#print(d)

for w in d:
	word[w] = d.count(w)

for key, value in word.items():
	print key,value


