
f =open('rosalind_dna.txt','r')
d = f.read()
#print(d[1])

A=0
C=0
G=0
T=0

for a in d:
	if a == 'A':
		A += 1
	elif a == 'C':
		C += 1
	elif a == 'G':
		G += 1
	elif a == 'T':
		T += 1

print 'A=',A,'C=',C,'G=',G,'T=',T

